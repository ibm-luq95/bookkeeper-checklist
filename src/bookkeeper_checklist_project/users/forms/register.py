from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"
        # fields = ("email",)
