from django.apps import AppConfig


class AccountConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    #Damit signals.py auch ausgeführt wird
    def ready(self):
        import account.signals
