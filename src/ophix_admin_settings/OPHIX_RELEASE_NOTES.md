# Ophix Admin Settings Release Notes

## 2026.10.04.01

- Reworked `README.md`'s opening with a hook-first pitch (instance identity and environment
  labelling — knowing which server you're looking at before you edit it), as part of the
  16-package taskserver-release-wave README overhaul.

## 2026.09.26.01

- Verified real compatibility under Python 3.14 (not just added the classifier) as part of the taskserver-release-wave compatibility sweep, and added `Programming Language :: Python :: 3.14` to the package classifiers.

## 2026.06.11.01

- Added `message_autohide_enabled` and `message_autohide_delay` fields to `ServerSettings`.
  When enabled, success and info message banners are automatically dismissed after the
  configured delay (default 4000 ms). Errors and warnings are never auto-hidden.
  Exposed in the new "Notifications" section of the Server Settings admin page.

## 2026.06.09.02

- Added `export_settings` management command — exports the `ServerSettings` singleton
  to a JSON file for backup or server migration.
- Added `import_settings` management command — imports from an `export_settings` file;
  applies only fields present in the file, reports per-field changes, supports `--dry-run`.
- Updated server-settings docs: removed stale "Visible in favicon" row, updated env badge
  colour description, added Backup and Migration section.

## 2026.05.31.01

- Initial release. Provides the `ServerSettings` singleton model for instance-specific
  configuration: server title, environment label, and language chooser settings.
- Settings survive theme changes and are independent of the active theme.
- Title is pre-populated from `SERVER_NAME` in `.env` on first `migrate` if blank.
- Context processor `ophix_admin_settings.context_processors.settings_context` injects
  `server_settings` into every admin template context via the `CONTEXT_PROCESSORS_APPEND`
  plugin mechanism (requires `ophix-server-base>=2026.05.31.01`).
