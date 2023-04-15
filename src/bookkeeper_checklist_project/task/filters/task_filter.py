# -*- coding: utf-8 -*-#
import django_filters
from django import forms

from bookkeeper.models import get_all_bookkeepers_as_choices
from task.models import Task


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            # "task_type": ["exact"],
            "status": ["exact"],
            "title": ["icontains"],
            "job__title": ["icontains"],
            "job__managed_by": ["exact"],
            # "job__bookkeeper": ["exact"]
            # "company_name": ["icontains"],
        }
