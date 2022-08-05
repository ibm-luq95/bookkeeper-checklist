from django.contrib.auth.forms import AuthenticationForm
from django import forms
from users.models import CustomUser

class CustomUserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ["user_type", "email", "password"]
 
        


