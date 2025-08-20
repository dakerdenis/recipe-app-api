# C:\...\django-basics\leads\urls.py
from django.urls import path
from . import views

app_name = "leads"
urlpatterns = [
    path("new/", views.create_lead, name="new"),
    path("", views.list_leads, name="list"),
]
