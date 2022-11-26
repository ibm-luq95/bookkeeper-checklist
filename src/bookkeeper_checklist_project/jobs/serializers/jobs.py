from rest_framework import serializers
from jobs.models import Job
from task.serializers import TaskSerializer
from client.serializers import ClientSerializer


class CreateJobSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    # client = ClientSerializer()

    class Meta:
        model = Job
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1
