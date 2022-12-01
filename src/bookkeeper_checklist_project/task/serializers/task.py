# -*- coding: utf-8 -*-#
from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = (
            "metadata",
            "is_deleted",
            "user",
            "deleted_at",
            "updated_at",
        )
        depth = 1
