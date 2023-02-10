# -*- coding: utf-8 -*-#
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from core.constants.form import CREATE_USER_FORM_FIELDS, EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin
from manager.models import Manager


class ManagerForm(BaseModelFormMixin, UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ManagerForm, self).__init__(*args, **kwargs)
        self.fields["user_type"].initial = "manager"
        self.fields["user_type"].widget.attrs.update(
            {"readonly": "readonly", "class": "readonly-select cursor-not-allowed"}
        )

    class Meta(BaseModelFormMixin.Meta):
        model = get_user_model()
        # exclude = EXCLUDED_FIELDS + ["user"]
        fields = CREATE_USER_FORM_FIELDS

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = "manager"
        if commit:
            user.save()
        Manager.objects.create(user=user)
        return user
