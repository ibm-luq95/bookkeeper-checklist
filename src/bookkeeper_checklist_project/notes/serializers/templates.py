# -*- coding: utf-8 -*-#
from rest_framework import serializers

from core.constants import EXCLUDED_FIELDS
from notes.models import NoteTemplate


class NoteTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteTemplate
        exclude = EXCLUDED_FIELDS
