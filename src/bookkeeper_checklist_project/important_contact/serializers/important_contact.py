# -*- coding: utf-8 -*-#
from rest_framework import serializers

from client.models import Client
from core.constants import EXCLUDED_FIELDS
from core.serializers import CreatedBySerializerMixin
from core.utils import debugging_print
from important_contact.models import ImportantContact
from django.db import transaction


class ImportantContactSerializer(serializers.ModelSerializer, CreatedBySerializerMixin):
    client = serializers.UUIDField(required=True)

    class Meta:
        model = ImportantContact
        exclude = EXCLUDED_FIELDS
        depth = 1

    def create(self, validated_data):
        client_pk = validated_data.get("client", None)
        client_pk = validated_data.pop("client")
        with transaction.atomic():
            instance = ImportantContact.objects.create(**validated_data)
            if client_pk is not None:
                client_object = Client.objects.select_related().filter(pk=client_pk).first()
                client_object.important_contacts.add(instance)
                client_object.save()

        return instance
