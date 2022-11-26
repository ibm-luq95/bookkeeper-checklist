# -*- coding: utf-8 -*-#
from rest_framework import serializers
from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1
