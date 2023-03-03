from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import Note, NoteTemplate


@admin.register(Note)
class NoteAdmin(BaseAdminModelMixin):
    pass


@admin.register(NoteTemplate)
class NoteTemplateAdmin(BaseAdminModelMixin):
    pass
