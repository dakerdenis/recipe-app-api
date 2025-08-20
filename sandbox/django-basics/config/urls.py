from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
    path("info/", include("info.urls")),
    path("leads/", include("leads.urls")),
]
