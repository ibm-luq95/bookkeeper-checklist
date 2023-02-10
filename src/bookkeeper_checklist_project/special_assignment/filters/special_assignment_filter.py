# -*- coding: utf-8 -*-#
from special_assignment.models import SpecialAssignment
import django_filters


class SpecialAssignmentFilter(django_filters.FilterSet):
    class Meta:
        model = SpecialAssignment
        fields = {
            "title": ["icontains"],
            "client__name": ["exact"],
            "status": ["exact"],
            "assigned_by": ["exact"],
            "is_seen": ["exact"],
        }
