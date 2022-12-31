# -*- coding: utf-8 -*-#
from assistant.models import Assistant
from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin


class AssistantForm(BaseModelFormMixin):
    def __init__(self, *args, **kwargs):
        super(AssistantForm, self).__init__(*args, **kwargs)

    class Meta(BaseModelFormMixin.Meta):
        model = Assistant
        exclude = EXCLUDED_FIELDS + ["user"]
        # fields = "__all__"
