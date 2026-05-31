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
| **Visible in favicon** | Show or hide the coloured dot overlaid on the favicon. |

The colour of the environment badge is controlled by **env color** in the theme editor (Header section), not here. This separation means the badge colour can be adapted per theme while the label text remains fixed.

---

## Language Chooser

Controls whether operators can switch the admin UI language from the page header.

| Setting | Description |
| --- | --- |
| **Active** | Show or hide the language chooser in the header. |
| **Control** | Dropdown style: Default Select or Minimal Select. |
| **Display** | Show language as its two-letter code (e.g. `EN`) or full name (e.g. `English`). |

The language chooser only appears when `USE_I18N = True`, at least two languages are configured in `LANGUAGES`, and `LocaleMiddleware` is active.
