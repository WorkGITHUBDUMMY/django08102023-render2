from django.shortcuts import render
from django.http import HttpResponse
from .models import GoodMorning

# Create your views here.
def home(request):
    try:
        goodmorning_obj = GoodMorning.objects.all()

        for items in goodmorning_obj:
            if items.time:
                if items.am_pm == "am":
                    context = "Morning to Noon"
                else:
                    context = "Noon to Night"
            else:
                context = "You are not alive, not selected"
        return render(request, 'base.html', {'context':context, })
    
    except:
        context = "You are not alive, table value not exists"
        return render(request, 'base.html', {'context':context, })
    