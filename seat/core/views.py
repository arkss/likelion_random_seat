from django.shortcuts import render, redirect
from .models import Babylion

def main(request):
    lions = Babylion.objects.all()
    par_lions=Babylion.objects.filter(part=True).order_by('?')
        
    context = {
        'lions':lions,
        'par_lions':par_lions,
    }

    return render(request, 'core/main.html', context)

def random(request):
    lions = Babylion.objects.all()
    part_list = []
    if request.method == "POST":

        for lion in lions:
            if request.POST.get(lion.name) == "on":
                lion.part = True
                lion.save()
            else:
                lion.part = False
                lion.save()
    return redirect('main')
