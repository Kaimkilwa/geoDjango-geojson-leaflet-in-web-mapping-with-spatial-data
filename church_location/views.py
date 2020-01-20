from django.shortcuts import render
from django.views.generic import DetailView
from .models import ChurchDetails

# Create your views here.

# Create your views here.
def home(request):
    return render(request, 'home/home_page.html')

def video_play(request):
    return render(request, 'home/video_play.html')

def TestMap(request ):
    qs = ChurchDetails.objects.filter(pk = 2)
    return render(request,'home/testing.html',{'qs':qs})

def Testing2(request):
    qs = ChurchDetails.objects.filter(pk=2)
    return render(request, 'home/test2.html', {'qs': qs})
