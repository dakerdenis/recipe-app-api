from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('health/', views.health, name='health'),
    path('admin/', views.admin, name='admin'),
    path('time/',views.time, name='time'),
]
