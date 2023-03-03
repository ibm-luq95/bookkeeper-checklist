# -*- coding: utf-8 -*-#
from django import forms

from core.forms import BaseModelFormMixin
from notes.models import NoteTemplate


class NoteTemplateForm(BaseModelFormMixin):
    def __int__(self, *args, **kwargs):
        super(NoteTemplateForm, self).__init__(*args, **kwargs)

    class Meta(BaseModelFormMixin.Meta):
        model = NoteTemplate
