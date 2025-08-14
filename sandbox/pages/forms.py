from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(
        label="Your name",
        min_length=2,
        max_length=100,
        help_text="Введите не короче 2 символов",
    )

    # Пример простой доп.валидации поля
    def clean_your_name(self):
        name = self.cleaned_data['your_name'].strip()
        if any(ch.isdigit() for ch in name):
            raise forms.ValidationError("Имя не должно содержать цифры.")
        return name
