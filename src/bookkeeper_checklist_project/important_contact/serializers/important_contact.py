# -*- coding: utf-8 -*-#
from rest_framework import serializers

from core.constants import EXCLUDED_FIELDS
from important_contact.models import ImportantContact


class ImportantContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImportantContact
        exclude = EXCLUDED_FIELDS
        # depth = 1
