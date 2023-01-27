# -*- coding: utf-8 -*-#
from notes.models import Note
from core.forms import BaseModelFormMixin, SaveCreatedByFormMixin


class NoteForm(BaseModelFormMixin, SaveCreatedByFormMixin):
    def __init__(self, client=None, note_section=None, created_by=None, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
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
