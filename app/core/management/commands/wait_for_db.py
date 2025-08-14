"""
    Django command for wait for the database to be available
    
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database to load"""
    
    def handle(self, *args, options):
        pass