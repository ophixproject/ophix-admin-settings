"""
ophix-manage export_settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Export the ServerSettings singleton to a JSON file for backup or server migration.

No passphrase option is provided: ServerSettings contains no sensitive data
(title, environment badge, language chooser). Protect the file with filesystem
permissions as you would any configuration file.

Use --stable to omit the meta block and sort keys, so re-exporting unchanged
settings produces byte-identical output (used by ophix-revisions).

Examples
--------
Export settings:
    ophix-manage export_settings --output-file settings.json

Deterministic export (for ophix-revisions):
    ophix-manage export_settings --output-file settings.json --stable

Preview (shows current values without writing):
    ophix-manage export_settings --output-file settings.json --dry-run
"""

import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError


def _build_meta(command: str) -> dict:
    import datetime
    import os
    import socket

    try:
        import pwd
        run_by = pwd.getpwuid(os.getuid()).pw_name
    except Exception:
        run_by = os.environ.get("USER") or os.environ.get("LOGNAME")

    from django.conf import settings
    ssh_raw = os.environ.get("SSH_CLIENT", "")
    return {
        "created_at":     datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "server_name":    getattr(settings, "SERVER_NAME", None),
        "server_version": getattr(settings, "SERVER_VERSION", None),
        "hostname":       socket.gethostname(),
        "command":        command,
        "run_by":         run_by,
        "login_user":     os.environ.get("SUDO_USER") or None,
        "ssh_origin":     ssh_raw.split()[0] if ssh_raw else None,
    }


def _serialize(obj) -> dict:
    return {
        "title":                     obj.title,
        "title_visible":             obj.title_visible,
        "env_name":                  obj.env_name,
        "env_visible_in_header":     obj.env_visible_in_header,
        "env_color":                 obj.env_color,
        "env_color_dark_use":        obj.env_color_dark_use,
        "env_color_dark":            obj.env_color_dark,
        "env_text_color":            obj.env_text_color,
        "env_text_color_dark_use":   obj.env_text_color_dark_use,
        "env_text_color_dark":       obj.env_text_color_dark,
        "message_autohide_enabled":  obj.message_autohide_enabled,
        "message_autohide_delay":    obj.message_autohide_delay,
        "language_chooser_active":   obj.language_chooser_active,
        "language_chooser_control":  obj.language_chooser_control,
        "language_chooser_display":  obj.language_chooser_display,
    }


class Command(BaseCommand):
    help = "Export the ServerSettings singleton to a JSON file for backup or server migration."

    def add_arguments(self, parser):
        parser.add_argument(
            "--output-file",
            required=True,
            metavar="FILE",
            help="Destination file path.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Print the values that would be exported without writing the file.",
        )
        parser.add_argument(
            "--stable",
            action="store_true",
            help="Omit the meta block and sort keys, so re-exporting unchanged settings "
                 "produces byte-identical output (used by ophix-revisions).",
        )
        parser.add_argument(
            "--quiet",
            action="store_true",
            help="Suppress all output.",
        )

    def handle(self, *args, **options):
        from ophix_admin_settings.models import ServerSettings

        output_path = Path(options["output_file"])
        dry_run     = options["dry_run"]
        stable      = options["stable"]
        quiet       = options["quiet"]

        obj = ServerSettings.load()
        data = _serialize(obj)

        if dry_run:
            if not quiet:
                self.stdout.write("Dry run — current ServerSettings values:")
                for field, value in data.items():
                    self.stdout.write(f"  {field}: {value!r}")
            return

        if not output_path.parent.exists():
            raise CommandError(f"Output directory does not exist: {output_path.parent}")

        payload = {"version": 1}
        if not stable:
            payload["meta"] = _build_meta("export_settings")
        payload["settings"] = data

        with output_path.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, sort_keys=stable)

        if not quiet:
            self.stdout.write(self.style.SUCCESS(
                f"ServerSettings exported to {output_path}."
            ))
