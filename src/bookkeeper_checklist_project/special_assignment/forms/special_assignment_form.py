# -*- coding: utf-8 -*-#
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin
from special_assignment.models import SpecialAssignment


class SpecialAssignmentForm(BaseModelFormMixin):
    def __init__(self, *args, **kwargs):
        super(SpecialAssignmentForm, self).__init__(*args, **kwargs)

    class Meta(BaseModelFormMixin.Meta):
        model = SpecialAssignment
        exclude = EXCLUDED_FIELDS + ["is_seen"]
