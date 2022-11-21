# -*- coding: utf-8 -*-#
from rest_framework import serializers
from company_services.models import CompanyService


class CreateCompanyServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyService
        exclude = (
            "metadata",
            "is_deleted",
        )
        # depth = 1
