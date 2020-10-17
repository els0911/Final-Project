import csv

from django.core.management.base import BaseCommand
from sightings.models import Squirrel
            
class Command(BaseCommand):  
    help = ("Exporting data to .csv")
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
    
    def handle(self,*args, **options):
        meta = {
            'file': 'csv_file',
            'class': Squirrel,
            'fields': ('X', 'Y', 'Unique Squirrel ID', 'Shift', 'Date', 'Age', 'Primary Fur Color', 'Location', 'Specific Location', 'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other Activities', 'Kuks', 'Quaas', 'Moans', 'Tail flags', 'Tail twitches', 'Approaches', 'Indifferent', 'Runs from') 
            # models fields you want to include 
        }
        self._write_csv(meta)

    def _write_csv(self, meta):
        """
        :param meta: (dict) keys should be 'file' (string: absolute path), 'class' the Python class
        object, 'fields' a list or tuple of field model field names (strings)
        """
        f = open(meta['file'], 'w+')
        writer = csv.writer(f)
        writer.writerow( meta['fields'] )
        for obj in meta['class'].objects.all():
            row = [unicode(getattr(obj, field)) for field in meta['fields']]
            writer.writerow(row)
        f.close()
