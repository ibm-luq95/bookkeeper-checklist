# -*- coding: utf-8 -*-#
from rest_framework import serializers

from company_services.helpers import PasswordHasher
from company_services.models import CompanyService
from core.serializers import CreatedBySerializerMixin


class CreateCompanyServicesSerializer(
    serializers.ModelSerializer, CreatedBySerializerMixin
):
    class Meta:
        model = CompanyService
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1

    def validate_password(self, value):
        encrypted = PasswordHasher.encrypt(value)
        return encrypted
