# -*- coding: utf-8 -*-#
from rest_framework import serializers
from special_assignment.models import SpecialAssignment


class SpecialAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialAssignment
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1
