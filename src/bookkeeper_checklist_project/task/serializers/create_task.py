# -*- coding: utf-8 -*-#
from rest_framework import serializers
from task.models import Task


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data["start_date"] > data["due_date"]:
            raise serializers.ValidationError(
                {"due_date": "Due date must occur after start date"}
            )
        return data
