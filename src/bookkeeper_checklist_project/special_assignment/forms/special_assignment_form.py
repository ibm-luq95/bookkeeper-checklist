# -*- coding: utf-8 -*-#
from django import forms
from django_summernote.fields import SummernoteTextFormField

from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin, SetSummernoteDynamicAttrsMixin
from core.utils import debugging_print
from special_assignment.models import SpecialAssignment


class SpecialAssignmentForm(BaseModelFormMixin, SetSummernoteDynamicAttrsMixin):
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

    body = SummernoteTextFormField()
    notes = SummernoteTextFormField(required=False)

    def __init__(self, assigned_by, set_full_width=False, *args, **kwargs):
        super(SpecialAssignmentForm, self).__init__(*args, **kwargs)
        SetSummernoteDynamicAttrsMixin.__init__(self, set_full_width=set_full_width)
        self.fields["assigned_by"].initial = assigned_by
        self.fields["assigned_by"].widget.attrs.update(
            {"class": "readonly-select cursor-not-allowed", "readonly": "readonly"}
        )

    class Meta(BaseModelFormMixin.Meta):
        model = SpecialAssignment
        exclude = EXCLUDED_FIELDS + ["is_seen"]
