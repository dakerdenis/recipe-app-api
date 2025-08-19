from django.urls import path
from . import views

app_name = "info"
urlpatterns = [ 
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
    path("subscribe/", views.subscribe, name="subscribe"),
    path("callback/", views.callback, name="callback"),
]
