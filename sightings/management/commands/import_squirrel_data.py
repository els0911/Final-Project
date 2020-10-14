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
                print(dict_)
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
                obj.Running=dict_['Running'].lower() == 'true'
                obj.Chasing=dict_['Chasing'].lower() == 'true'
                obj.Climbing=dict_['Climbing'].lower() == 'true'
                obj.Eating=dict_['Eating'].lower() == 'true'
                obj.Foraging=dict_['Foraging'].lower() == 'true'
                obj.Other_Activities=dict_['Other Activities']
                obj.Kuks=dict_['Kuks'].lower() == 'true'
                obj.Quaas=dict_['Quaas'].lower() == 'true'
                obj.Moans=dict_['Moans'].lower() == 'true'
                obj.Tail_Flags=dict_['Tail flags'].lower() == 'true'
                obj.Tail_Twitches=dict_['Tail twitches'].lower() == 'true'
                obj.Approaches=dict_['Approaches'].lower() == 'true'
                obj.Indifferent=dict_['Indifferent'].lower() == 'true'
                obj.Runs_From=dict_['Runs from'].lower() == 'true'
                print(obj)
                obj.save()

        msg = f'You imported the file'
