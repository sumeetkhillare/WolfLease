"""
    This is the application starting point where you can register different modules. 
"""

from django.apps import AppConfig



class HousingConfig(AppConfig):
    """
    This is configuration for Housing Module.
    
    """
    default_auto_field = 'django.db.models.BigAutoField'  
    '''Default autofields '''
    name = 'housing'

