# -*- coding: utf-8 -*-#
import django_filters
from notes.models import Note


class NotesFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = {
            "title": ["icontains"],
            "note_section": ["exact"],
            "client": ["exact"],
            "job": ["exact"],
            "task": ["exact"],
            "body": ["icontains"],
        }
