from django.shortcuts import render
  
from django.shortcuts import get_object_or_404, redirect

from django.http import JsonResponse

from .forms import AddForm

from django.db.models import Avg, Max, Min, Count, Q

from .models import Squirrel


def index(request):
    squirrels=Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }

    return render(request, 'sightings/index.html', context)

def update(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=squirrel_id)
    if request.method == 'POST':
        form = AddForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = AddForm(instance=squirrel)

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
    Age = squirrels.values_list('Age').annotate(Count('Age'))
    Primary_Fur_Color = squirrels.values_list('Primary_Fur_Color').annotate(Count('Primary_Fur_Color'))
    Location = squirrels.values_list('Location').annotate(Count('Location'))
    Running = squirrels.values_list('Running').annotate(Count('Running'))
    Chasing = squirrels.values_list('Chasing').annotate(Count('Chasing'))
    Climbing = squirrels.values_list('Climbing').annotate(Count('Climbing'))
    Eating = squirrels.values_list('Eating').annotate(Count('Eating'))
    Foraging = squirrels.values_list('Foraging').annotate(Count('Foraging'))
    Chasing = squirrels.values_list('Chasing').annotate(Count('Chasing'))

    context = {'Number': len(squirrels),
            'Latitude': squirrels.aggregate(average=Avg('Latitude')),
            'Longitude': squirrels.aggregate(average=Avg('Longitude')),
            'Age_Adult': Age[2][1],
            'Age_Juvenile': Age[3][1],
            'Black': Primary_Fur_Color[1][1],
            'Cinnamon': Primary_Fur_Color[2][1],
            'Gray': Primary_Fur_Color[3][1],
            'Above_Ground': Location[1][1],
            'Ground_Plane': Location[2][1],
            'Running': Running[1][1],
            'Chasing': Chasing[1][1],
            'Climbing': Climbing[1][1],
            'Eating': Eating[1][1],
            'Foraging': Foraging[1][1],
            'Chasing': Chasing[1][1],
    }

    return render(request, 'sightings/stats.html', context)
