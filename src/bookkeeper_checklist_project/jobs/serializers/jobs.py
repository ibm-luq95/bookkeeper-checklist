from rest_framework import serializers

from core.constants import EXCLUDED_FIELDS
from jobs.models import Job
from task.serializers import TaskSerializer
from bookkeeper.serializers import BookkeeperSerializer


class CreateJobSerializer(serializers.ModelSerializer):
    # tasks = TaskSerializer(many=True, read_only=True)
    # client = ClientSerializer()

    class Meta:
        model = Job
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1


class JobSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    bookkeeper = BookkeeperSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        exclude = EXCLUDED_FIELDS
        depth = 2
