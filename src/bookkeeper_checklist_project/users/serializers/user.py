from rest_framework import serializers

from core.constants import EXCLUDED_FIELDS
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = EXCLUDED_FIELDS + ["password", "created_at"]
        depth = 1
