# -*- coding: utf-8 -*-#
from rest_framework import serializers

from core.constants import EXCLUDED_FIELDS
from documents.serializers import DocumentTemplateSerializer
from jobs.models import JobTemplate
from notes.serializers import NoteTemplateSerializer
from task.serializers import TaskTemplateSerializer


class JobTemplateSerializer(serializers.ModelSerializer):
    documents = DocumentTemplateSerializer(many=True)
    tasks = TaskTemplateSerializer(many=True)
    notes = NoteTemplateSerializer(many=True)
    status_display = serializers.CharField(source="get_status_display", required=False)
    type_display = serializers.CharField(source="get_job_type_display", required=False)

    class Meta:
        model = JobTemplate
        exclude = EXCLUDED_FIELDS
        depth = 1
