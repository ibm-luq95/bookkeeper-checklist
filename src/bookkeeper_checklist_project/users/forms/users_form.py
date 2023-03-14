# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import Permission
from django.db import transaction
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.safestring import mark_safe

from assistant.models import Assistant
from bookkeeper.models import Bookkeeper
from core.constants.form import CREATE_USER_FORM_FIELDS
from core.forms import BaseModelFormMixin
from core.forms.widgets import CustomPasswordInputWidget

from core.utils import debugging_print
from manager.models import Manager
from users.models import CustomUser


class UserCreationForm(UserCreationForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """

    password1 = forms.CharField(label="Password", widget=CustomPasswordInputWidget)
    password2 = forms.CharField(
        label="Password confirmation", widget=CustomPasswordInputWidget
    )

    class Meta:
        model = CustomUser
        fields = CREATE_USER_FORM_FIELDS + ["is_superuser", "is_active"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        with transaction.atomic():
            permission_codename = None
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            if user.user_type == "manager":
                permission_codename = "manager_user"
                Manager.objects.create(user=user)
            elif user.user_type == "bookkeeper":
                permission_codename = "bookkeeper_user"
                Bookkeeper.objects.create(user=user)
            elif user.user_type == "assistant":
                permission_codename = "assistant_user"
                Assistant.objects.create(user=user)
            user.user_permissions.add(Permission.objects.get(codename=permission_codename))
            return user


class UserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    def __init__(
        self,
        password_url=None,
        user_object: Optional[CustomUser] = None,
        *args,
        **kwargs,
    ):
        if user_object:
            all_initial_permissions = []
            content_type_object = ContentType.objects.filter(
                model__in=[
                    # user_object.user_type,
                    "Client",
                    "CompanyService",
                    "Job",
                    "JobTemplate",
                    "JobCategory",
                    "Task",
                    "SpecialAssignment",
                    "Discussion",
                    "Documents",
                    "ImportantContact",
                    "ClientAccount",
                    "Note",
                ]
            )
            # for group in user_object.groups.all():
            #     all_initial_permissions = [perm for perm in group.permissions.all()]
            all_initial_permissions = [perm for perm in user_object.user_permissions.all()]
            # debugging_print(all_initial_permissions)
            permissions = [perm for perm in content_type_object]
            # debugging_print(Permission.objects.filter(content_type__in=content_type_object))
            self.base_fields[
                "user_permissions"
            ] = forms.ModelMultipleChoiceField(  # this should before super().__init__
                queryset=Permission.objects.filter(content_type__in=permissions),
                label="Set custom permissions",
                # initial=all_initial_permissions,
                # widget=forms.CheckboxSelectMultiple,
                widget=forms.SelectMultiple,
                help_text=mark_safe(
                    "<strong>** Press CTRL in keyboard when pick permissions to avoid lose the previous "
                    "permissions **</strong>"
                ),
            )
            # debugging_print(all_initial_permissions)
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            password.help_text = password.help_text.replace(
                "../password/", str(password_url)
            )

            # debugging_print(all_permissions)

        # password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = CREATE_USER_FORM_FIELDS + [
            "password",
            "is_superuser",
            "is_active",
            "user_permissions",
            # "groups",
        ]


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password", widget=CustomPasswordInputWidget)

    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # class Meta:
    #     model = get_user_model()
    #     fields = ("password",)
