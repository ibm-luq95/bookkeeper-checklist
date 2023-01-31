# -*- coding: utf-8 -*-#
from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    task_type_display = serializers.CharField(source="get_task_type_display")
    task_status_display = serializers.CharField(source="get_task_status_display")

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

    def update(self, instance, validated_data):
        instance = super(TaskSerializer, self).update(instance, validated_data)
        # for tag_data in tags_data:
        #     tag_qs = Tag.objects.filter(name__iexact=tag_data['name'])
        #
        #     if tag_qs.exists():
        #         tag = tag_qs.first()
        #     else:
        #         tag = Tag.objects.create(**tag_data)
        #
        #     instance.tag.add(tag)

        return instance
