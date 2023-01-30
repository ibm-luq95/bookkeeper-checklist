# -*- coding: utf-8 -*-#
from django.utils import timezone
from rest_framework import serializers

from core.serializers import CreatedBySerializerMixin
from task.models import Task


class CreateTaskSerializer(serializers.ModelSerializer, CreatedBySerializerMixin):
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
        now = timezone.now()
        if data["start_date"] > data["due_date"]:
            raise serializers.ValidationError(
                {"due_date": "Due date must occur after start date"}
            )
        if data["start_date"] < now.date():
            raise serializers.ValidationError(
                {"start_date": "Start date not valid, it is old!"}
            )
        if data["due_date"] < now.date():
            raise serializers.ValidationError(
                {"due_date": "Due date not valid, it is old!"}
            )

        return data
