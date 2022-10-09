from django.apps import AppConfig

"""
    This is the application starting point where you can register different modules. 
"""

class HousingConfig(AppConfig):
    """
    This is configuration for Housing Module.
    
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'housing'

