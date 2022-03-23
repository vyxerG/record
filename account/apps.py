from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    def ready(self):
        import account.signals  # Tells django to search inside our usersApp then check inside the submodule by name signals it will then see the Handlers
