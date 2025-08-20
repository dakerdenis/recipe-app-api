from django.contrib import admin
from .models import Guest

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("name", "message", "created_at")
    search_fields = ("name",)
    list_filter=("created_at",)
# Register your models here.
