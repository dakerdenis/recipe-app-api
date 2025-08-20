from django import forms
from django.core.exceptions import ValidationError
import re

class ContactForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=50)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Сообщение", widget=forms.Textarea, max_length=2000)

class SubsribeForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=50)
    email = forms.EmailField(label="Email для подписки")
    agree_to_terms = forms.BooleanField(label="I agree to the terms and conditions", required=True)
    
    
class CallbackForm(forms.Form):
    CONTACT_CHOICES = [("email", "Email"), ("phone", "Телефон")]
    full_name = forms.CharField(label="Ваше имя", max_length=50)
    contact_method = forms.ChoiceField(
        choices=CONTACT_CHOICES,
        widget=forms.RadioSelect,
        label="Select an option:"
    )
    email = forms.EmailField(
        label="Email для связи",
        required=False,
        max_length=50)
    
    phone = forms.CharField(
        label="Телефон",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "+994 55 555 55 55"}),
        max_length=50)
    
    details = forms.CharField(
        label="Кратко о запросе",
        widget=forms.Textarea,
        min_length=20,
        max_length=500)    
    
    agree_to_terms = forms.BooleanField(label="I agree to the terms and conditions")    
    hp_code = forms.CharField(required=False, widget=forms.TextInput(attrs={"autocomplete": "off"}))
    
    def clean_full_name(self):
        value = self.cleaned_data["full_name"].strip()
        if len(value.split()) < 2:
            raise ValidationError("Укажите имя и фамилию.")
        return value
    
    def clean_phone(self):
        value = self.cleaned_data.get("phone","")
        if not value:
            return value
        if not re.fullmatch(r"[0-9\+\-\s\(\)]+", value):
            raise ValidationError("телефон в нормальный вид идиот")
        digits = re.sub(r"\D", "", value)
        if len(digits) < 10:
            raise ValidationError("Введите минимум 10 цифр")
        return value
    
    def clean(self):
        cleaned = super().clean() #все данные прошедшие валидацию собираются cleaned_data
        
        """
        Следующие 4 поля - из cleaned_data 
        get - вернёт None - если данные не прошли валидацию или их нет
        """
        method = cleaned.get("contact_method")
        email = cleaned.get("email")
        phone = cleaned.get("phone")
        hp = cleaned.get("hp_code")
        
        if hp:
            raise ValidationError("Спам активность")
        #Проверка на спам 
        if method == "email" and not email:
            self.add_error("email", "Укажите эмейл")
        if method == "phone" and not phone:
            self.add_error("phone","Укажи телфон ебанат")
            
        return cleaned
        