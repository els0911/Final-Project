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
            
            unique = [] 
            for dict_ in reader:
                if dict_['Unique Squirrel ID'] in unique:
                    continue
                else:
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
                    obj.Running=True if dict_['Running'].lower() == 'true' else False
                    obj.Chasing=True if dict_['Chasing'].lower() == 'true' else False
                    obj.Climbing=True if dict_['Climbing'].lower() == 'true' else False
                    obj.Eating=True if dict_['Eating'].lower() == 'true' else False
                    obj.Foraging=True if dict_['Foraging'].lower() == 'true' else False
                    obj.Other_Activities=dict_['Other Activities']
                    obj.Kuks=True if dict_['Kuks'].lower() == 'true' else False
                    obj.Quaas=True if dict_['Quaas'].lower() == 'true' else False
                    obj.Moans=True if dict_['Moans'].lower() == 'true' else False
                    obj.Tail_Flags=True if dict_['Tail flags'].lower() == 'true' else False
                    obj.Tail_Twitches=True if dict_['Tail twitches'].lower() == 'true' else False
                    obj.Approaches=True if dict_['Approaches'].lower() == 'true' else False
                    obj.Indifferent=True if dict_['Indifferent'].lower() == 'true' else False
                    obj.Runs_From=True if dict_['Runs from'].lower() == 'true' else False
                    obj.save()
                    unique.append(dict_['Unique Squirrel ID'])
