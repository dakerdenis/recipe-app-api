from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('health/', views.health, name='health'),
    path('time/', views.time_now, name='time'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    # path('custom-admin/', views.custom_admin_login, name='custom_admin'),  # по желанию
]
