# C:\...\django-basics\leads\forms.py
from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["full_name", "email", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }
