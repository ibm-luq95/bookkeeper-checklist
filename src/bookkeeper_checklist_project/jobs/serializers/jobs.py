from django.utils import timezone
from rest_framework import serializers

from bookkeeper.serializers import BookkeeperSerializer
from assistant.serializers import AssistantSerializer
from client.models import Client
from client.serializers import ClientSerializer
from core.choices import JobTypeEnum, JobStatusEnum
from core.constants import EXCLUDED_FIELDS
from core.serializers import CreatedBySerializerMixin
from jobs.models import Job, JobProxy, JobCategory
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

    # due_date = serializers.DateField(read_only=True)

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


class JobOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    job_type = serializers.ChoiceField(choices=JobTypeEnum.choices)
    status = serializers.ChoiceField(choices=JobStatusEnum.choices)
    state = serializers.ChoiceField(choices=JobStatusEnum.choices)
    categories = serializers.PrimaryKeyRelatedField(
        queryset=JobCategory.objects.all(), many=True
    )

    class Meta:
        depth = 1
