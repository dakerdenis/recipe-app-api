from django import forms
from django.core.exceptions import ValidationError

class GuestForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=50)
    message = forms.CharField(label="Your message", widget=forms.Textarea, max_length=1000)

    def clean_name(self):
        value = self.cleaned_data["name"].strip()
        if len(value.split()) < 2:
            raise ValidationError("Укажите имя и фамилию.")
        return value
