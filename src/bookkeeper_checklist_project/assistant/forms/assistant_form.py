# -*- coding: utf-8 -*-#
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from core.constants.form import CREATE_USER_FORM_FIELDS
from assistant.models import Assistant
from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin


class AssistantForm(BaseModelFormMixin, UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AssistantForm, self).__init__(*args, **kwargs)
        self.fields["user_type"].initial = "assistant"
        self.fields["user_type"].widget.attrs.update(
            {"readonly": "readonly", "class": "readonly-select cursor-not-allowed"}
        )

    class Meta(BaseModelFormMixin.Meta):
        model = get_user_model()
        # exclude = EXCLUDED_FIELDS + ["user"]
        fields = CREATE_USER_FORM_FIELDS

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = "assistant"
        if commit:
            user.save()
        Assistant.objects.create(user=user)
        return user
