from django.shortcuts import render
from .forms import ProductForm
from .models import Product

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)  # <-- request.FILES обязателен
        if form.is_valid():
            form.save()  # сохранит запись в БД и файл в MEDIA_ROOT/upload_to
            return render(request, "shop/new.html", {"form": ProductForm(), "sent": True})
    else:
        form = ProductForm()
    return render(request, "shop/new.html", {"form": form})

def product_list(request):
    items = Product.objects.order_by("-created_at")[:50]
    return render(request, "shop/list.html", {"items": items})
