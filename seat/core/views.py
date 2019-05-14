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
                part_list.append(lion)
            else:
                lion.part = False
                
        par_lion=Babylion.objects.filter(part="True").order_by('?')
        

        for i in par_lion:
            print(i,"@@")
        
    return redirect('main')