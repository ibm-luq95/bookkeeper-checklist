# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms
from documents.models import Documents
from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin, SaveCreatedByFormMixin, RemoveFieldsMixin


class DocumentForm(BaseModelFormMixin, SaveCreatedByFormMixin, RemoveFieldsMixin):
    # auto_id = "doct_"

    def __init__(
        self,
        document_section=None,
        client=None,
        is_update=False,
        created_by=None,
        removed_fields: Optional[list] = None,
        *args,
        **kwargs,
    ):
        super(DocumentForm, self).__init__(*args, **kwargs)
        RemoveFieldsMixin.__init__(self, removed_fields=removed_fields)
        if document_section is not None:
            self.fields["document_section"].initial = document_section
            # self.fields["document_section"].widget.attrs.update({"class": "readonly-select cursor-not-allowed"})
            # self.fields.pop("task")
            self.fields.pop("job")

        # if client is not None:
        #     self.fields["client"].initial = client

        if is_update is True:
            self.fields["document_file"].required = False
            self.fields["document_file"].widget.attrs["readonly"] = True

        if created_by is not None:
            self.created_by = created_by

    class Meta(BaseModelFormMixin.Meta):
        model = Documents
        exclude = EXCLUDED_FIELDS
