# -*- coding: utf-8 -*-#
from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1
