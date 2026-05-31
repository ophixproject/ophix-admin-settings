# Ophix Admin Settings Release Notes

## 2026.05.31.01

- Initial release. Provides the `ServerSettings` singleton model for instance-specific
  configuration: server title, environment label, and language chooser settings.
- Settings survive theme changes and are independent of the active theme.
- Title is pre-populated from `SERVER_NAME` in `.env` on first `migrate` if blank.
- Context processor `ophix_admin_settings.context_processors.settings_context` injects
  `server_settings` into every admin template context via the `CONTEXT_PROCESSORS_APPEND`
  plugin mechanism (requires `ophix-server-base>=2026.05.31.01`).
