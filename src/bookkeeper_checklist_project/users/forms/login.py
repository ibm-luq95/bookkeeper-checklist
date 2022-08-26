# from django.contrib.auth.forms import AuthenticationForm
from django import forms
from core.choices import CustomUserTypeEnum


class CustomUserLoginForm(forms.Form):
    user_type = forms.ChoiceField(
        label="User Type", choices=CustomUserTypeEnum.choices, required=True
    )
    email = forms.EmailField(label="Email Address", required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
