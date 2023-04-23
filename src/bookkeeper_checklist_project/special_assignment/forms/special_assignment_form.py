# -*- coding: utf-8 -*-#
from django import forms

from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin, JoditFormMixin
from core.utils import debugging_print
from special_assignment.models import SpecialAssignment


class SpecialAssignmentForm(BaseModelFormMixin, JoditFormMixin):
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

    def __init__(self, assigned_by, add_jodit_css_class=False, *args, **kwargs):
        super(SpecialAssignmentForm, self).__init__(*args, **kwargs)
        JoditFormMixin.__init__(self, add_jodit_css_class=add_jodit_css_class)
        self.fields["assigned_by"].initial = assigned_by
        self.fields["assigned_by"].widget.attrs.update(
            {"class": "readonly-select cursor-not-allowed", "readonly": "readonly"}
        )

    class Meta(BaseModelFormMixin.Meta):
        model = SpecialAssignment
        exclude = EXCLUDED_FIELDS + ["is_seen"]
