from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request, "pages/home.html", {"title": "Home page"})

def time(request):
    
    return render(request, "pages/time.html",{"title": "Time page", "current_time": timezone.now()})

def hello(request): 
    return HttpResponse("stalker")