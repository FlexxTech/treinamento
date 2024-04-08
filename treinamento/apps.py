from django.apps import AppConfig


class TreinamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'treinamento'

    def ready(self):
        import treinamento.signals