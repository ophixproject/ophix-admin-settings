---
title: Server Settings
slug: server-settings
order: 520
section: Extensions
---

# Server Settings

**Server Settings** holds instance-specific configuration — values that identify this particular server and should survive a theme change. Switching from one theme to another does not alter any setting here.

Access it via **Settings** in the admin sidebar.

---

## Server Identity

| Setting | Description |
| --- | --- |
| **Title** | Displayed first in the browser tab (`TaskServer \| Page Name`) and in the admin header. Pre-populated from `SERVER_NAME` in `.env` on first install if blank. |
| **Title visible** | Whether the title text appears in the admin header alongside the logo. |

---

## Environment

A short label that identifies the deployment environment. Useful when multiple instances of the same domain are running (e.g. production, staging, and dev).

| Setting | Description |
| --- | --- |
| **Environment name** | The label text, e.g. `Production`, `Staging`, `Dev`. |
| **Visible in header** | Show or hide the environment badge in the page header. |
| **Badge color** | Background colour of the environment badge (light and optional dark variant). |
| **Badge text color** | Text colour of the environment badge (light and optional dark variant). |

---

## Language Chooser

Controls whether operators can switch the admin UI language from the page header.

| Setting | Description |
| --- | --- |
| **Active** | Show or hide the language chooser in the header. |
| **Control** | Dropdown style: Default Select or Minimal Select. |
| **Display** | Show language as its two-letter code (e.g. `EN`) or full name (e.g. `English`). |

The language chooser only appears when `USE_I18N = True`, at least two languages are configured in `LANGUAGES`, and `LocaleMiddleware` is active.

---

## Backup and Migration

`export_settings` and `import_settings` let you preserve and restore the ServerSettings singleton — useful when migrating to a new server or cloning a staging environment.

**Export:**

```bash
ophix-manage export_settings --output-file settings.json
```

**Preview current values without writing:**

```bash
ophix-manage export_settings --output-file settings.json --dry-run
```

**Import (applies all fields from the file):**

```bash
ophix-manage import_settings --input-file settings.json
```

**Preview what would change:**

```bash
ophix-manage import_settings --input-file settings.json --dry-run
```

Import is safe to re-run — fields that already match the current values are reported as unchanged. Fields present in the file but absent from the model are ignored with a warning; fields absent from the file are left at their current values.
