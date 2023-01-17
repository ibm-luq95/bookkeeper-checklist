# -*- coding: utf-8 -*-#
from django import forms
from documents.models import Documents
from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin, Html5Mixin


class DocumentForm(BaseModelFormMixin, Html5Mixin):
    # auto_id = "doct_"

    def __init__(
        self, document_section=None, client=None, is_update=False, *args, **kwargs
    ):
        super(DocumentForm, self).__init__(*args, **kwargs)
        if document_section is not None:
            self.fields["document_section"].initial = document_section
            # self.fields["document_section"].widget.attrs.update({"class": "readonly-select cursor-not-allowed"})
            # self.fields.pop("task")
            self.fields.pop("job")

        if client is not None:
            self.fields["client"].initial = client

        if is_update is True:
            self.fields["document_file"].required = False
            self.fields["document_file"].widget.attrs["readonly"] = True

    class Meta(BaseModelFormMixin.Meta):
        model = Documents
        exclude = EXCLUDED_FIELDS + ["user"]
