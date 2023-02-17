# -*- coding: utf-8 -*-#
from django.utils import timezone
from rest_framework import serializers

from client.models import Client
from core.serializers import CreatedBySerializerMixin
from jobs.models import Job
from task.models import Task


class TaskSerializer(serializers.ModelSerializer, CreatedBySerializerMixin):
    task_type_display = serializers.CharField(
        source="get_task_type_display", required=False
    )
    task_status_display = serializers.CharField(
        source="get_task_status_display", required=False
    )
    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all(), many=False)

    class Meta:
        model = Task
        # fields = ("get_task_type_display",)
        exclude = (
            "metadata",
            "is_deleted",
            # "user",
            "deleted_at",
            "updated_at",
            "is_completed",
        )
        depth = 1

    # def update(self, instance, validated_data):
    #     instance = super(TaskSerializer, self).update(instance, validated_data)
    #     # for tag_data in tags_data:
    #     #     tag_qs = Tag.objects.filter(name__iexact=tag_data['name'])
    #     #
    #     #     if tag_qs.exists():
    #     #         tag = tag_qs.first()
    #     #     else:
    #     #         tag = Tag.objects.create(**tag_data)
    #     #
    #     #     instance.tag.add(tag)
    #
    #     return instance

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
