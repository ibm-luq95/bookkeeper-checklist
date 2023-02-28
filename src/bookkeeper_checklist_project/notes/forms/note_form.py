# -*- coding: utf-8 -*-#
from typing import Optional
from notes.models import Note
from core.forms import BaseModelFormMixin, SaveCreatedByFormMixin, RemoveFieldsMixin


class NoteForm(BaseModelFormMixin, SaveCreatedByFormMixin, RemoveFieldsMixin):
    def __init__(
        self,
        client=None,
        note_section=None,
        created_by=None,
        removed_fields: Optional[list] = None,
        *args,
        **kwargs,
    ):
        super(NoteForm, self).__init__(*args, **kwargs)
        RemoveFieldsMixin.__init__(self, removed_fields=removed_fields)
        if client is not None:
            self.fields["client"].initial = client
            self.fields.pop("task")
            self.fields.pop("job")
        if note_section is not None:
            self.fields["note_section"].initial = note_section

        if created_by is not None:
            self.created_by = created_by

    class Meta(BaseModelFormMixin.Meta):
        model = Note
        # fields = "__all__"
