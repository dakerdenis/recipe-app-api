from django.shortcuts import render
from .forms import GuestForm
from .models import Guest

def create_guest(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            return render(
                request,
                "guestbook/new.html", {
                    "form": GuestForm(),
                    "send": True,
                    "data": data,
                }
            )
    else:
        form = GuestForm()
    return render(request, "guestbook/new.html", {
        "form": form,
        "title": "Pizda"
    })
    
        
def list_guest(request):
    guests = Guest.objects.order_by("-created_at")[:50]
    return render(request, "guestbook/list.html", {
        "title": "Pizda",
        "guests": guests
    })


