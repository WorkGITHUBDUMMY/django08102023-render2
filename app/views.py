from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GoodMorning

# Create your views here.
def home(request):
    try:
        goodmorning_obj = GoodMorning.objects.get(id=5)
        print(goodmorning_obj.time_hour)
        if goodmorning_obj.time_hour:
            if goodmorning_obj.am_pm == "am":
                context = "Morning to Noon"
            else:
                context = "Noon to Night"

        return render(request, 'base.html', {'context':context, })
    
    except:
        context = "You are not alive, table value not exists"
        return render(request, 'base.html', {'context':context, })

from .forms import Form1
def form(request):
    if request.method == "POST":
        form = Form1(request.POST)
        form.save()
        return redirect('home')
    else:
        form = Form1()
    return render(request, 'form.html', {'form': form, })
