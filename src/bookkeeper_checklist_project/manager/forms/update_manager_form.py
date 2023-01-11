# -*- coding: utf-8 -*-#
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from core.constants.form import CREATE_FORM_FIELDS, EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin
from manager.models import Manager


class ManagerUpdateForm(BaseModelFormMixin):
    def __init__(self, *args, **kwargs):
        super(ManagerUpdateForm, self).__init__(*args, **kwargs)
        self.fields.pop("company_services")

    class Meta(BaseModelFormMixin.Meta):
        model = Manager
        exclude = EXCLUDED_FIELDS + ["user"]
        # fields = CREATE_FORM_FIELDS
