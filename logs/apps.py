from django.apps import AppConfig


class LogsConfig(AppConfig):
    name = 'logs'

    def ready(self):
        # Load signals Admin login
        import logs.signal
