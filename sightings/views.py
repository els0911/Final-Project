from django.shortcuts import render
  
from django.shortcuts import get_object_or_404, redirect

from django.http import JsonResponse

from .forms import AddForm, UpdateForm

from django.db.models import Avg, Max, Min, Count

from .models import Squirrel


def index(request):
    squirrels=Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }

    return render(request, 'sightings/index.html', context)

def update(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=squirrel_id)
    context = {
            'squirrel': squirrel,
        }
    return render(request, 'sightings/update.html', context)
    if request.method == 'POST':
        form = AddForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{Unique_Squirrel_ID}')
    else:
        form = AddForm()

    context = {
        'form': form,
    }
    return render(request, 'sightings/update.html', context) 


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = AddForm()

    context = {
        'form': form,
    }
    return render(request, 'sightings/add.html', context)

def stats(request):
    squirrels=Squirrel.objects.all()
    context = {'amount': len(squirrels),
            'latitude': squirrels.aggregate(minimum=Min('Latitude'),maximum=Max('Latitude')),
            'longitude': squirrels.aggregate(minimum=Min('Longitude'),maximum=Max('Longitude')),
            'primary_fur_color': list(squirrels.values_list('Primary_Fur_Color').annotate(Count('Primary_Fur_Color'))),
            'running': list(squirrels.values_list('Running').annotate(Count('Running'))),
            'shift': list(squirrels.values_list('Shift').annotate(Count('Shift'))),
    }

    return render(request, 'sightings/stats.html', context)
