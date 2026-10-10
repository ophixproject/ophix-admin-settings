plugin_category = "core"
plugin_sort = 30

default_app_config = "ophix_admin_settings.apps.OphixAdminSettingsConfig"


def get_revisions_targets():
    """
    Optional hook discovered by ophix-revisions (if installed). Unencrypted —
    ServerSettings holds no sensitive data (title, environment badge,
    language chooser), same reasoning export_settings' own docstring gives
    for shipping no passphrase option at all.
    """
    return [
        {
            "name": "settings",
            "app_label": "ophix_admin_settings",
            # Precise model match — export_settings exports the ServerSettings
            # singleton only.
            "models": ["ophix_admin_settings.serversettings"],
            "export_command": "export_settings",
            "encrypted": False,
            "stable": True,
        },
    ]
