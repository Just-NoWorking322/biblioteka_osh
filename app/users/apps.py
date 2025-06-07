from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.users'
    verbose_name = "Регистрация"
    
def ready(self):
    import users.signals  # noqa
