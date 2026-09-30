# ophix-admin-settings

**Know which server you're looking at, every time** — instance identity and environment labelling for every [Ophix](https://ophix.io) server.

Running the same admin UI across a dozen servers makes it easy to lose track of which one is actually in front of you — and that's exactly the moment someone edits production thinking it's staging. `ophix-admin-settings` gives every server its own title and a visible environment badge (Production, Staging, Dev, or whatever you call it), right in the header and favicon, so there's never any doubt.

This package is automatically included in every Ophix server, no need to separately install it.

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
