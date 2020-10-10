from django.shortcuts import render

from django.shortcuts import get_object_or_404

from django.http import JsonResponse

from .forms import AdoptRequestForm

from .models import Pet


def index(request):
    pets = Pet.objects.all()
    context = {
            'pets': pets,
    }

    return render(request, 'adopt/index.html', context)


def detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    context = {
            'pet': pet,
    }

    return render(request, 'adopt/detail.html', context)

def adopt_request(request):
    if request.method == 'POST':
        form = AdoptRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    
    return JsonResponse({}, status=405)
