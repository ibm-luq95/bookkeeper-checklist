# -*- coding: utf-8 -*-#
import django_filters
from django import forms

from bookkeeper.models import get_all_bookkeepers_as_choices
from task.models import Task


class TaskFilter(django_filters.FilterSet):
    # job__bookkeeper = django_filters.ChoiceFilter(
    #     widget=forms.Select(), choices=get_all_bookkeepers_as_choices, label="Bookkeeper"
    # )

    class Meta:
        model = Task
        fields = {
            "task_type": ["exact"],
            "task_status": ["exact"],
            "job__title": ["icontains"],
            # "job__bookkeeper": ["exact"]
            # "company_name": ["icontains"],
        }
