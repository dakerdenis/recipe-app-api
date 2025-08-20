from django.shortcuts import render
from .forms import GuestForm
from .models import Guest

def create_guest(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            # ручное сохранение в БД через модель
            Guest.objects.create(
                name=form.cleaned_data["name"],
                message=form.cleaned_data["message"],
            )
            return render(
                request,
                "guestbook/new.html",
                {"form": GuestForm(), "sent": True}  # <<< в шаблоне проверяешь sent
            )
    else:
        form = GuestForm()

    return render(request, "guestbook/new.html", {"form": form, "title": "Guestbook"})

    
        
def list_guest(request):
    guests = Guest.objects.order_by("-created_at")[:50]
    return render(request, "guestbook/list.html", {
        "title": "Pizda",
        "guests": guests
    })


