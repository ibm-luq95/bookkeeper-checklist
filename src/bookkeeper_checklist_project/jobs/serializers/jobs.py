from django.utils import timezone
from rest_framework import serializers

from bookkeeper.serializers import BookkeeperSerializer
from assistant.serializers import AssistantSerializer
from client.models import Client
from client.serializers import ClientSerializer
from core.constants import EXCLUDED_FIELDS
from core.serializers import CreatedBySerializerMixin
from jobs.models import Job, JobProxy
from task.serializers import TaskSerializer
from users.models import CustomUser


class CreateJobSerializer(serializers.ModelSerializer, CreatedBySerializerMixin):
    class Meta:
        model = JobProxy
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1

    def validate(self, data):
        """
        Check that start is before finish.
        """
        now = timezone.now().date()
        if data["due_date"] < now:
            raise serializers.ValidationError({"due_date": "Due date old!"})
        return data


class JobSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), many=False)
    managed_by = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), many=False, allow_null=True
    )

    # bookkeeper = BookkeeperSerializer(many=True, read_only=True)
    # assistants = AssistantSerializer(many=True, read_only=True)

    class Meta:
        model = JobProxy
        exclude = EXCLUDED_FIELDS
        depth = 3

    def validate(self, data):
        """
        Check that start is before finish.
        """
        now = timezone.now().date()
        if data["due_date"] < now:
            raise serializers.ValidationError({"due_date": "Due date old!"})
        return data
