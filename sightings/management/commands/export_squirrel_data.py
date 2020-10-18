import csv
  
from django.core.management.base import BaseCommand
from sightings.models import Squirrel 

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        file_=options['csv_file']
        with open(file_, 'w', newline='') as csvfile:
            writer=csv.writer(csvfile,quoting=csv.QUOTE_ALL)
            writer.writerow(['X',
                        'Y', 
                        'Unique Squirrel ID', 
                        'Shift', 
                        'Date', 
                        'Age', 
                        'Primary Fur Color', 
                        'Location',
                        'Specific Location',
                        'Running',
                        'Chasing',
                        'Climbing',
                        'Eating',
                        'Foraging',
                        'Other Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
                        'Tail flags',
                        'Tail twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs from'])
            fields = ['Latitude', 
            	        'Longitude', 
            		'Unique_Squirrel_ID', 
            		'Shift', 
            		'Date', 
            		'Age', 
            		'Primary_Fur_Color', 
            		'Location',
                        'Specific_Location',
                        'Running',
                        'Chasing',
                        'Climbing',
                        'Eating',
                        'Foraging',
                        'Other_Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
                        'Tail_Flags',
                        'Tail_Twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs_From']
            for obj in Squirrel.objects.all():
                writer.writerow([getattr(obj, field) for field in fields])
