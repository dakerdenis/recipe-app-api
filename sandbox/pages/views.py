from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

def home(request):
    return render(request, 'home.html', {'title': 'Home'})
def about(request):
    return render(request, 'about.html', {'title': 'About'})
def health(request):
    return JsonResponse({"status": "pizda"})
def admin(request):
    return render(request,'admin/login.html', {'title': 'Admin login'})
def time(request):
    now = timezone.now()
    return render(request, 'time.html', {'title': 'Current time', 'current_time': now})
