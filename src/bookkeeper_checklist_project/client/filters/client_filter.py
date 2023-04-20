# -*- coding: utf-8 -*-#
import django_filters
from django import forms

from bookkeeper.models import BookkeeperProxy
from client.models import ClientProxy


class ClientFilter(django_filters.FilterSet):
    bookkeepers = django_filters.ModelMultipleChoiceFilter(
        field_name="bookkeepers",
        queryset=BookkeeperProxy.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        lookup_expr="exact",
    )

    class Meta:
        model = ClientProxy
        fields = {
            "name": ["icontains"],
            # "managed_by": ["exact"],
            "industry": ["icontains"],
            "important_contacts__company_name": ["icontains"],
            "important_contacts__contact_label": ["icontains"],
        }
