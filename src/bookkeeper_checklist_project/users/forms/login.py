from django.contrib.auth.forms import AuthenticationForm
from users.models import CustomUser

class CustomUserLoginForm(AuthenticationForm):
    # fields = "__all__"
    class Meta:
        fields = "__all__"
        model = CustomUser
        


