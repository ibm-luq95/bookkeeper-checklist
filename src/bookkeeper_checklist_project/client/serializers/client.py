# -*- coding: utf-8 -*-#
from rest_framework import serializers
from client.models import Client
from core.serializers import CreatedBySerializerMixin


class ClientSerializer(serializers.ModelSerializer, CreatedBySerializerMixin):
    class Meta:
        model = Client
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1
