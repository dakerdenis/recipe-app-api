from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path("", views.home, name="home"),
    path("time/", views.time, name="time"),
    path("hello/", views.hello, name="hello"),
]
