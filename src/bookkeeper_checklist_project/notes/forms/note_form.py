# -*- coding: utf-8 -*-#
from notes.models import Note
from core.forms import BaseModelFormMixin


class NoteForm(BaseModelFormMixin):
    def __init__(self, client=None, note_section=None, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields.pop("user")
        if client is not None:
            self.fields["client"].initial = client
            self.fields.pop("task")
            self.fields.pop("job")
        if note_section is not None:
            self.fields["note_section"].initial = note_section

    class Meta(BaseModelFormMixin.Meta):
        model = Note
        # fields = "__all__"
