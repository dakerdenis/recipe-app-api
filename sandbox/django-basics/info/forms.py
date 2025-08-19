from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=50)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Сообщение", widget=forms.Textarea, max_length=2000)

class SubsribeForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=50)
    email = forms.EmailField(label="Email для подписки")
    agree_to_terms = forms.BooleanField(label="I agree to the terms and conditions", required=True)
    
    
class CallbackForm(forms.Form):
    full_name = forms.CharField(label="Ваше имя", max_length=50)
    contact_method = forms.ChoiceField(
        choices=[
            ('email', 'Email'),
            ('phone', 'Мобильный телефон'),
        ],
        widget=forms.RadioSelect,
        label="Select an option:"
    )
    email = forms.EmailField(label="Email для связи")
    phone = forms.CharField(label="Ваше имя", max_length=50)
    details = forms.CharField(widget=forms.Textarea, min_length=20, max_length=500)
    agree_to_terms = forms.BooleanField(label="I agree to the terms and conditions", required=True)
    