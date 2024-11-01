from django.apps import AppConfig


class HousingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    '''Default autofields '''
    name = 'housing'

    def ready(self):
        import housing.signals
        print(housing.signals)
