# -*- coding: utf-8 -*-#
from rest_framework import serializers
from core.serializers.job_template_create import SaveRelatedJobTemplateSerializer
from core.constants import EXCLUDED_FIELDS
from task.models import TaskTemplate


class TaskTemplateSerializer(
    SaveRelatedJobTemplateSerializer, serializers.ModelSerializer
):
    task_type_display = serializers.CharField(
        source="get_task_type_display", required=False
    )
    status_display = serializers.CharField(source="get_status_display", required=False)

    class Meta:
        model = TaskTemplate
        # exclude = EXCLUDED_FIELDS
        depth = 2
        fields = [
            "title",
            "job_template",
            "notes",
            "task_type",
            "status",
            "attachment",
            "items",
            "status_display",
            "task_type_display"
        ]
