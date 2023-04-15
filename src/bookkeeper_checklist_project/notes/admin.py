# from django_summernote.admin import SummernoteModelAdmin

from core.admin import BaseAdminModelMixin, SummernoteAdminMixin
from django.contrib import admin

from .models import Note, NoteTemplate


@admin.register(Note)
class NoteAdmin(BaseAdminModelMixin, SummernoteAdminMixin):
    pass


@admin.register(NoteTemplate)
class NoteTemplateAdmin(BaseAdminModelMixin, SummernoteAdminMixin):
    pass
