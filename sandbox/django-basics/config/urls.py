from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
    path("info/", include("info.urls")),
    path("leads/", include("leads.urls")),
    path("guestbook/", include("guestbook.urls")),
    path("shop/", include("shop.urls")),  # добавим позже файл shop/urls.py
]


# только для разработки:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)