from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'API'
    def ready(self):
        from API import scheduler
        scheduler.start()
