from django.shortcuts import render, redirect
from .models import Babylion
import random

def main(request):
    lions = Babylion.objects.all()
    context = {
        'lions':lions,
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

        par_lion=Babylion.objects.filter(part="True").order_by('?')
        print(par_lion)

        # for i in par_lion:
        #     print(i,"@@")

    return redirect('main')
