# from django_summernote.admin import SummernoteModelAdmin

from core.admin import BaseAdminModelMixin, JoditEditorAdminMixin
from django.contrib import admin

from .models import Note, NoteTemplate


@admin.register(Note)
class NoteAdmin(BaseAdminModelMixin, JoditEditorAdminMixin):
    pass


@admin.register(NoteTemplate)
class NoteTemplateAdmin(BaseAdminModelMixin, JoditEditorAdminMixin):
    pass
