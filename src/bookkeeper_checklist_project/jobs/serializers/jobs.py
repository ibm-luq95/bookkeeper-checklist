from django.utils import timezone
from rest_framework import serializers

from bookkeeper.serializers import BookkeeperSerializer
from core.constants import EXCLUDED_FIELDS
from core.serializers import CreatedBySerializerMixin
from jobs.models import Job
from task.serializers import TaskSerializer


class CreateJobSerializer(serializers.ModelSerializer, CreatedBySerializerMixin):
    class Meta:
        model = Job
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
    bookkeeper = BookkeeperSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        exclude = EXCLUDED_FIELDS
        depth = 2
