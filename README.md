# ophix-admin-settings

Instance settings for [Ophix Project](https://ophix.io) servers — server identity, environment label, and language chooser configuration.

This package is automatically installed as a dependency of `ophix-admin-interface`. It is not a domain plugin; it applies to every Ophix server regardless of which domain is installed.

---

## What it does

Provides a singleton **Server Settings** admin page containing settings that are instance-specific rather than theme-specific. These settings survive theme changes — switching from one theme to another does not alter the server's identity or environment label.

| Setting | Description |
| --- | --- |
| **Title** | Displayed in the browser tab and admin header (e.g. `TaskServer`, `CredServer`) |
| **Title visible** | Toggle title display in the admin header |
| **Environment name** | Short label shown in the header and favicon (e.g. `Production`, `Staging`, `Dev`) |
| **Env visible in header** | Show or hide the environment badge in the page header |
| **Env visible in favicon** | Show or hide the environment marker on the favicon |
| **Language chooser** | Active, control style (default/minimal), and display format (code/name) |

---

## Installation

Installed automatically with `ophix-admin-interface`. To install explicitly:

```bash
pip install ophix-admin-settings
```

Run migrations after installation:

```bash
ophix-manage migrate
```

On first `migrate`, the **title** field is pre-populated from the `SERVER_NAME` setting in `.env` if it is blank.

---

## Docs import

```bash
ophix-manage update_docs --include-app-docs ophix.core,ophix_admin_settings,ophix_docs
```
