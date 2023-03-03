# -*- coding: utf-8 -*-#
from rest_framework import serializers

from core.constants import EXCLUDED_FIELDS
from task.models import TaskTemplate


class TaskTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTemplate
        exclude = EXCLUDED_FIELDS
