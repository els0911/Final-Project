from django.forms import ModelForm

from .models import Squirrel


class AddForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = [
            'Latitude',
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
            'Runs_From',
        ]
