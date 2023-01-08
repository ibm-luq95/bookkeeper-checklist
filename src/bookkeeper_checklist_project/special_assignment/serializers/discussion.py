# -*- coding: utf-8 -*-#
from rest_framework import serializers
from special_assignment.models import Discussion, SpecialAssignment


class DiscussionSerializer(serializers.ModelSerializer):
    special_assignment = serializers.PrimaryKeyRelatedField(
        queryset=SpecialAssignment.objects.all(), many=False
    )

    class Meta:
        model = Discussion
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1
