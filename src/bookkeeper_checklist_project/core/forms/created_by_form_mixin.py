# -*- coding: utf-8 -*-#
from typing import Any

from django import forms


class SaveCreatedByFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        abstract = True

    def save(self, commit=True) -> Any:
        obj = super().save(commit=False)
        if hasattr(self, "created_by"):
            obj.created_by = self.created_by
        if commit:
            obj.save()
        return obj
