from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ("first_name", "last_name", "email", "user_type",)
