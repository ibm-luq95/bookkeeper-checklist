# -*- coding: utf-8 -*-#
from django import forms
from documents.models import DocumentTemplate
from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin, SaveCreatedByFormMixin, RemoveFieldsMixin


class DocumentTemplateForm(BaseModelFormMixin):
    def __int__(self, *args, **kwargs):
        super(DocumentTemplateForm, self).__init__(*args, **kwargs)

    class Meta(BaseModelFormMixin.Meta):
        model = DocumentTemplate
        exclude = EXCLUDED_FIELDS
