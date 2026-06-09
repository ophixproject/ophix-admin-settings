"""
ophix-manage import_settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Import ServerSettings from a JSON file produced by export_settings.

All fields in the file are applied to the singleton. Fields absent from the
file are left unchanged, so a partial export file (e.g. only env_* fields) is
safe to import — unmentioned fields keep their current values.

Examples
--------
Import settings:
    ophix-manage import_settings --input-file settings.json

Preview without writing:
    ophix-manage import_settings --input-file settings.json --dry-run
"""

import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError


_FIELD_TYPES = {
    "title":                    str,
    "title_visible":            bool,
    "env_name":                 str,
    "env_visible_in_header":    bool,
    "env_color":                str,
    "env_color_dark_use":       bool,
    "env_color_dark":           str,
    "env_text_color":           str,
    "env_text_color_dark_use":  bool,
    "env_text_color_dark":      str,
    "language_chooser_active":  bool,
    "language_chooser_control": str,
    "language_chooser_display": str,
}

_VALID_CHOICES = {
    "language_chooser_control": {"default-select", "minimal-select"},
    "language_chooser_display": {"code", "name"},
}


class Command(BaseCommand):
    help = "Import ServerSettings from a JSON file produced by export_settings."

    def add_arguments(self, parser):
        parser.add_argument(
            "--input-file",
            required=True,
            metavar="FILE",
            help="Source file path (JSON produced by export_settings).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Show what would change without making any changes.",
        )
        parser.add_argument(
            "--quiet",
            action="store_true",
            help="Suppress per-field output. Summary line is always shown.",
        )

    def handle(self, *args, **options):
        from ophix_admin_settings.models import ServerSettings

        input_path = Path(options["input_file"])
        dry_run    = options["dry_run"]
        quiet      = options["quiet"]

        if not input_path.exists():
            raise CommandError(f"Input file not found: {input_path}")

        try:
            payload = json.loads(input_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise CommandError(f"Invalid JSON in {input_path}: {exc}")

        if not isinstance(payload, dict) or "settings" not in payload:
            raise CommandError("Unrecognised file format — expected export_settings output.")

        incoming = payload["settings"]
        if not isinstance(incoming, dict):
            raise CommandError("Expected 'settings' to be a JSON object.")

        obj = ServerSettings.load()
        changed = {}
        skipped = []

        for field, expected_type in _FIELD_TYPES.items():
            if field not in incoming:
                continue

            raw = incoming[field]

            if not isinstance(raw, expected_type):
                skipped.append(f"{field} (wrong type: expected {expected_type.__name__}, got {type(raw).__name__})")
                continue

            if field in _VALID_CHOICES and raw not in _VALID_CHOICES[field]:
                skipped.append(f"{field} (invalid choice: {raw!r})")
                continue

            current = getattr(obj, field)
            if current != raw:
                changed[field] = (current, raw)

        unknown = [k for k in incoming if k not in _FIELD_TYPES]
        if unknown:
            for k in unknown:
                self.stderr.write(f"  Unknown field ignored: {k!r}")

        if not quiet:
            if changed:
                for field, (old, new) in changed.items():
                    self.stdout.write(f"  {field}: {old!r} → {new!r}")
            else:
                self.stdout.write("  No fields differ from current settings.")

        if skipped:
            for note in skipped:
                self.stderr.write(f"  Skipped: {note}")

        if dry_run:
            summary = f"{len(changed)} field(s) would be updated" if changed else "nothing to do"
            self.stdout.write(f"Dry run: {summary}.")
            return

        if changed:
            for field, (_, new) in changed.items():
                setattr(obj, field, new)
            try:
                obj.full_clean()
                obj.save()
            except Exception as exc:
                raise CommandError(f"Failed to save ServerSettings: {exc}")
            self.stdout.write(self.style.SUCCESS(
                f"{len(changed)} field(s) updated."
            ))
        else:
            self.stdout.write("Settings unchanged — nothing to do.")
