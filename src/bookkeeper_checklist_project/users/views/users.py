from django.contrib.auth.views import LoginView
from users.forms import CustomUserLoginForm


class LoginView(LoginView):
    template_name: str = "users/login.html"
    form_class = CustomUserLoginForm
