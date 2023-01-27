# -*- coding: utf-8 -*-#
from rest_framework import serializers

from core.serializers import CreatedBySerializerMixin
from notes.models import Note


class CreateNoteSerializer(serializers.ModelSerializer, CreatedBySerializerMixin):
    class Meta:
        model = Note
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1
