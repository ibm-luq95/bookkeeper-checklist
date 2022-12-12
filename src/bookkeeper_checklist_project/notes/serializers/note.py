# -*- coding: utf-8 -*-#
from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1
