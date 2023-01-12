# -*- coding: utf-8 -*-#

from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import CustomUser


class UpdateUserForm(forms.ModelForm):
    def __init__(self, client=None, is_update=False, updated_object=None, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), required=False
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), required=False
    )

    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ("first_name", "last_name", "email", "user_type", "password")
