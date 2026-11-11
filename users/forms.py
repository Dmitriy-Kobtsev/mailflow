from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class BootstrapAuthenticationForm(AuthenticationForm):
    """Форма входа с Bootstrap-стилями и label по-русски.

    Наследуемся от AuthenticationForm: вся логика проверки email+пароля
    остаётся у Django. Переопределяем только отображение полей.
    """

    username = UsernameField(
        label="Email",
        widget=forms.TextInput(attrs={
            "autofocus": True,
            "class": "form-control",
            "placeholder": "you@example.com",
            "autocomplete": "username",
        }),
    )
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "••••••••",
            "autocomplete": "current-password",
        }),
    )