# -*- coding: utf-8 -*-#
import django_filters
from client.models import Client


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = {
            "name": ["icontains"],
            "industry": ["icontains"],
            "important_contacts__company_name": ["icontains"],
        }
