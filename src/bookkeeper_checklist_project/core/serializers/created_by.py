# -*- coding: utf-8 -*-#
from rest_framework import serializers
from users.models import CustomUser


class CreatedBySerializerMixin(serializers.Serializer):
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), many=False
    )
