# -*- coding: utf-8 -*-#
import django_filters
from django import forms

from jobs.models import JobTemplate


class JobTemplateFilter(django_filters.FilterSet):
    class Meta:
        model = JobTemplate
        # form = JobFilterForm
        fields = {
            "title": ["icontains"],
            "job_type": ["exact"],
            "status": ["exact"],
        }
