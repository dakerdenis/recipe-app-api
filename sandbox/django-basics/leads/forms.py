# C:\...\django-basics\leads\forms.py
from django import forms
from .models import Lead #модель

class LeadForm(forms.ModelForm):  #forms.ModelForm - django тут сам генерирует всё "модельная"форма
    class Meta:
        model = Lead  #привязывается модель - указываем с какой работаем
        fields = ["full_name", "email", "message"] #какие модели включить в форму
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Иван Иванов"}),
            "message": forms.Textarea(attrs={"rows": 5}),
        }
