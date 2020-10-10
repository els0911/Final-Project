from django.shortcuts import render
  
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

from .forms import AddForm

from .models import Squirrel


def index(request):
    squirrel =Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }

    return render(request, 'sightings/index.html', context)

