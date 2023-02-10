# -*- coding: utf-8 -*-#
import django_filters
from company_services.models import CompanyService


class CompanyServicesFilter(django_filters.FilterSet):
    class Meta:
        model = CompanyService
        fields = {
            "client__name": ["icontains"],
            "service_name": ["exact"],
            "label": ["exact"],
        }
