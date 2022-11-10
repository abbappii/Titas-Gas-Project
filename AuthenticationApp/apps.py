from django.apps import AppConfig


class AuthenticationappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AuthenticationApp'

    def ready(self):
        import AuthenticationApp.signals