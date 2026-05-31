_cached_settings = None


def get_cached_settings():
    global _cached_settings
    if _cached_settings is None:
        from .models import ServerSettings
        _cached_settings = ServerSettings.load()
    return _cached_settings


def del_cached_settings():
    global _cached_settings
    _cached_settings = None


def settings_context(request):
    return {"server_settings": get_cached_settings()}
