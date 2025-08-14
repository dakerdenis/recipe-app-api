from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import NameForm

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def about(request):
    return render(request, 'about.html', {'title': 'About'})

def health(request):
    # в проде — предсказуемый ответ
    return JsonResponse({"status": "ok"})

# Лучше не называть "admin", чтобы не путать со встроенной админкой
def custom_admin_login(request):
    return render(request, 'custom_admin/login.html', {'title': 'Admin login'})

def time_now(request):
    now = timezone.now()
    return render(request, 'time.html', {'title': 'Current time', 'current_time': now})

def contact(request):
    if request.method == "POST":
        form = NameForm(request.POST)             # связанная форма
        if form.is_valid():                       # валидация
            name = form.cleaned_data['your_name'] # безопасные данные
            # здесь можно сделать любое действие: логирование/письмо/сохранение
            request.session['contact_name'] = name  # временно сохраним имя
            return redirect('contact_success')       # PRG: редирект после POST
    else:
        form = NameForm()                         # незаполненная форма

    return render(request, 'contact.html', {
        'title': 'Contact form',
        'form': form
    })

def contact_success(request):
    name = request.session.pop('contact_name', None)
    return render(request, 'contact_success.html', {
        'title': 'Thanks',
        'name': name
    })
