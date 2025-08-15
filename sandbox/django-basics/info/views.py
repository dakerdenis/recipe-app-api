from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


def about(request):
    return render(request, "info/about.html", {"title": "О нас страница"})

def contacts(request):
    return render(request, "info/contacts.html", {"title": "Связь с нами"})

