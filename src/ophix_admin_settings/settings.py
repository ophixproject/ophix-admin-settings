from ophix.settings.utils import get_bool_env

CONTEXT_PROCESSORS_APPEND = [
    "ophix_admin_settings.context_processors.settings_context",
]

SHOW_SETTINGS_MODEL = get_bool_env("SHOW_SETTINGS_MODEL", default=False)
