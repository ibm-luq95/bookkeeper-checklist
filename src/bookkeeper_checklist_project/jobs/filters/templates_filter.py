# -*- coding: utf-8 -*-#
import django_filters
from django import forms

from jobs.models import JobTemplate, JobCategory


class JobTemplateFilter(django_filters.FilterSet):
    categories = django_filters.ModelMultipleChoiceFilter(
        field_name="categories",
        queryset=JobCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        lookup_expr="exact",
    )

    class Meta:
        model = JobTemplate
        # form = JobFilterForm
        fields = {
            "title": ["icontains"],
            "description": ["icontains"],
            "job_type": ["exact"],
            "status": ["exact"],
            "state": ["exact"],
            # "categories": ["exact"],
        }
