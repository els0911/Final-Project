import csv

from django.core.management.base import BaseCommand
from sightings.models import Squirrel


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        file_=options['csv_file']

        with open(file_) as fp:
            reader = csv.DictReader(fp)
            
        
            for dict_ in reader:
                obj = Squirrel()
                obj.Latitude=dict_['X']
                obj.Longitude=dict_['Y']
                obj.Unique_Squirrel_ID=dict_['Unique Squirrel ID']
                obj.Shift=dict_['Shift']
                obj.Date=dict_['Date'][4:]+'-'+dict_['Date'][:2]+'-'+dict_['Date'][2:4]
                obj.Age=dict_['Age']
                obj.Primary_Fur_Color=dict_['Primary Fur Color']
                obj.Location=dict_['Location']
                obj.Specific_Location=dict_['Specific Location']
                obj.Running=dict_['Running']
                obj.Chasing=dict_['Chasing']
                obj.Climbing=dict_['Climbing']
                obj.Eating=True if dict_['Eating'].lower() == 'true' else False
                
                obj.Foraging=dict_['Foraging']
                obj.Other_Activities=dict_['Other Activities']
                print(obj.Other_Activities)
                obj.Kuks=dict_['Kuks']
                obj.Quaas=dict_['Quaas']
                obj.Moans=dict_['Moans']
                obj.Tail_Flags=dict_['Tail flags']
                obj.Tail_Twitches=dict_['Tail twitches']
                obj.Approaches=dict_['Approaches']
                obj.Indifferent=dict_['Indifferent']
                obj.Runs_From=dict_['Runs from']
             
        


