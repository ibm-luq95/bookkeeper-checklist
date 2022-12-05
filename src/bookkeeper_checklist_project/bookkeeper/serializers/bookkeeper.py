from rest_framework import serializers

from core.constants import EXCLUDED_FIELDS
from bookkeeper.models import Bookkeeper
from users.serializers import UserSerializer


class BookkeeperSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Bookkeeper
        exclude = EXCLUDED_FIELDS
        depth = 1
