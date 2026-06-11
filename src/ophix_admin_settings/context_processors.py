def settings_context(request):
    from .models import ServerSettings
    return {"server_settings": ServerSettings.load()}
