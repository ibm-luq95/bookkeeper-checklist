# -*- coding: utf-8 -*-#
from rest_framework import serializers

from core.constants import EXCLUDED_FIELDS
from assistant.models import Assistant
from users.serializers import UserSerializer


class AssistantSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Assistant
        exclude = EXCLUDED_FIELDS
        depth = 1
