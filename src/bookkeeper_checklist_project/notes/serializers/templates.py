# -*- coding: utf-8 -*-#
from rest_framework import serializers


from core.serializers.job_template_create import SaveRelatedJobTemplateSerializer


from notes.models import NoteTemplate


class NoteTemplateSerializer(
    SaveRelatedJobTemplateSerializer, serializers.ModelSerializer
):
    class Meta:
        model = NoteTemplate
        # exclude = EXCLUDED_FIELDS
        fields = ["title", "body", "job_template"]
        # fields = "__all__"
        # depth = 2
