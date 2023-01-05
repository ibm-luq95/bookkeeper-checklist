# -*- coding: utf-8 -*-#
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from bookkeeper.models import Bookkeeper
from core.constants.form import CREATE_FORM_FIELDS
from core.forms import BaseModelFormMixin
from core.utils import debugging_print


class BookkeeperForm(BaseModelFormMixin, UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(BookkeeperForm, self).__init__(*args, **kwargs)
        self.fields["user_type"].initial = "bookkeeper"
        self.fields["user_type"].widget.attrs.update(
            {"readonly": "readonly", "class": "readonly-select"}
        )

    class Meta(BaseModelFormMixin.Meta):
        model = get_user_model()
        # exclude = EXCLUDED_FIELDS + ["last_login"]
        fields = CREATE_FORM_FIELDS

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = "bookkeeper"
        if commit:
            user.save()
        Bookkeeper.objects.create(user=user)
        return user
