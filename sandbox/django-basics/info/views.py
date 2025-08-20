from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .forms import ContactForm  # <-- добавили
from .forms import SubsribeForm  # <-- добавили
from .forms import CallbackForm  # <-- добавили

def about(request):
    if request.method == "POST":
        form = ContactForm(request.POST)          # наполняем форму данными из запроса
        if form.is_valid():                       # запускаем валидацию всех полей
            data = form.cleaned_data              # здесь уже "чистые" данные
            # тут позже будем СОХРАНЯТЬ в БД или слать email
            # пока просто покажем сообщение об успехе и пустую форму
            return render(
                request,
                "info/about.html",
                {"title": "О нас страница", "form": ContactForm(), "sent": True, "data": data},
            )
    else:
        form = ContactForm()                      # пустая форма для GET

    return render(request, "info/about.html", {"title": "О нас страница", "form": form})



def subscribe(request):
    if request.method == 'POST':
        form = SubsribeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render (
                request,
                "info/subscribe.html",
                {"title":"Подписка оформлена, спасибо !", "form": SubsribeForm(),"sent":True,"data":data},
            )
    else:
        form = SubsribeForm()      
    return render(request, "info/subscribe.html", {"title": "Оформить подписку", "form": form})






def callback(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["full_name"].split()[0]
            method = form.cleaned_data["contact_method"]
            return render(
                request,
                "info/callback.html",
                {"title": "Запрос обратной связи", 
                 "form": CallbackForm(), 
                 "sent": True,
                 "first_name": first_name, 
                 "method": method}
            )
        # НЕ создаём новую пустую форму! Падаем вниз и отрисуем форму с ошибками.
    else:
        form = CallbackForm()

    # ВАЖНО: всегда передаём form в контекст
    return render(request, "info/callback.html", {"title": "Запрос обратной связи", "form": form})





def contacts(request):
    return render(request, "info/contacts.html", {"title": "Связь с нами"})
