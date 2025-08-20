# C:\...\django-basics\leads\views.py
from django.shortcuts import render
from .forms import LeadForm
from .models import Lead

def create_lead(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()  # <-- ВОТ ЗДЕСЬ сохраняем в БД
            return render(request, "leads/new.html", {"form": LeadForm(), "sent": True})
    else:
        form = LeadForm()
    return render(request, "leads/new.html", {"form": form})

def list_leads(request):
    items = Lead.objects.order_by("-created_at")[:50]
    return render(request, "leads/list.html", {"items": items})
