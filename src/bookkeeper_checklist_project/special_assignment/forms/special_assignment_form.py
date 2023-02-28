# -*- coding: utf-8 -*-#
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django import forms
from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin
from special_assignment.models import SpecialAssignment


class SpecialAssignmentForm(BaseModelFormMixin):
    field_order = [
        "client",
        "title",
        "body",
        "attachment",
        "start_date",
        "due_date",
        "notes",
        "assigned_by",
        "status",
    ]

    def __init__(self, assigned_by, *args, **kwargs):
        super(SpecialAssignmentForm, self).__init__(*args, **kwargs)
        self.fields["assigned_by"].initial = assigned_by
        self.fields["assigned_by"].widget.attrs.update(
            {"class": "readonly-select cursor-not-allowed", "readonly": "readonly"}
        )

    class Meta(BaseModelFormMixin.Meta):
        model = SpecialAssignment
        exclude = EXCLUDED_FIELDS + ["is_seen"]
