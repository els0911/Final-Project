import csv

from django.core.management.base import BaseCommand
from django.utils import timezone
from sightings.models import Squirrel


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        with open(path) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        squirrels = []
        for dict_ in data:
            squirrels.append(Squirrel(
                Latitude=dict_[0],
                Longitude=dict_[1],
                Unique_Squirrel_ID=dict_[2],
                Shift=dict_[4],
                Date=dict_[5][4:]+'-'+dict_[5][:2]+'-'+dict_[5][2:4],
                Age=dict_[7],
                Primary_Fur_Color=dict_[8],
                Location=dict_[12],
                Specific_Location=dict_[14],
                Running=dict_[15].lower() == 'true',
                Chasing=dict_[16].lower() == 'true',
                Climbing=dict_[17].lower() == 'true',
                Eating=dict_[18].lower() == 'true',
                Foraging=dict_[19].lower() == 'true',
                Other_Activities=dict_[20],
                Kuks=dict_[21].lower() == 'true',
                Quaas=dict_[22].lower() == 'true',
                Moans=dict_[23].lower() == 'true',
                Tail_Flags=dict_[24].lower() == 'true',
                Tail_Twitches=dict_[25].lower() == 'true',
                Approaches=dict_[26].lower() == 'true',
                Indifferent=dict_[27].lower() == 'true',
                Runs_From=dict_[28].lower() == 'true'
            ))

        Squirrel.objects.bulk_create(squirrels)

