from django.urls import path
from . import views

app_name="guestbook"
urlpatterns = [
    path("new/", views.create_guest, name="new"),
    path("", views.list_guest, name="list"),
]
