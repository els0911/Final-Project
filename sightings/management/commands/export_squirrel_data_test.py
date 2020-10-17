import csv

from django.core.management.base import BaseCommand
from sightings.models import Squirrel
            
class Command(BaseCommand):  
    help = ("Exporting data to .csv")
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=open)
    
    def handle(self, *args, **options):
        
        with open('csv_file', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
                                                          
            writer.writerow(['X', 'Y', 'Unique Squirrel ID', 'Shift', 'Date', 'Age', 'Primary Fur Color', 'Location', 'Specific Location', 'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other Activities', 'Kuks', 'Quaas', 'Moans', 'Tail Flags', 'Tail Twitches', 'Approaches', 'Indifferent', 'Runs From'])
            csvfile.close() 
