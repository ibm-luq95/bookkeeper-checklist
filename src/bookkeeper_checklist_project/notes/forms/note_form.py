# -*- coding: utf-8 -*-#
from typing import Optional

# from django_summernote.fields import SummernoteTextFormField

from notes.models import Note
from core.forms import (
    BaseModelFormMixin,
    SaveCreatedByFormMixin,
    RemoveFieldsMixin,
    JoditFormMixin,
)


class NoteForm(
    BaseModelFormMixin,
    SaveCreatedByFormMixin,
    RemoveFieldsMixin,
    JoditFormMixin,
):
    # body = SummernoteTextFormField()

    def __init__(
        self,
        client=None,
        note_section=None,
        created_by=None,
        add_jodit_css_class=False,
        removed_fields: Optional[list] = None,
        *args,
        **kwargs,
    ):
        super(NoteForm, self).__init__(*args, **kwargs)
        RemoveFieldsMixin.__init__(self, removed_fields=removed_fields)
        JoditFormMixin.__init__(
            self, add_jodit_css_class=add_jodit_css_class
        )
        if client is not None:
            self.fields["client"].initial = client
            self.fields.pop("task")
            self.fields.pop("job")
        if note_section is not None:
            self.fields["note_section"].initial = note_section

        self.fields.pop("status")

        if created_by is not None:
            self.created_by = created_by

    class Meta(BaseModelFormMixin.Meta):
        model = Note
        # fields = "__all__"
        # widgets = {
        # "body": SummernoteWidget()
        # "body": SummernoteInplaceWidget()
        # }
