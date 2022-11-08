from rest_framework import serializers
from jobs.models import Job


class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ("metadata", "is_deleted",)
        # depth = 1
