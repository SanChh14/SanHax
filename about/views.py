from django.shortcuts import render
from gamesblog.models import Gamesblog
from appsblog.models import Appsblog
from itertools import chain
from operator import attrgetter

# Create your views here.

def about(request):
    apps= Appsblog.objects.all()
    games = Gamesblog.objects.all()
    trendings = sorted(chain(apps,games),key=attrgetter('views'),reverse=True)
    return render(request, 'about/about.html', {'trendings':trendings[:10]})
