# -*- coding: utf-8 -*-#
from django import template

from core.models import BaseQuerySetMixin

register = template.Library()


@register.filter(name="tasks_count_for_job")
def tasks_count_for_job(jobs_queryset: BaseQuerySetMixin) -> int:
    count_list = []
    for job in jobs_queryset:
        count_list.append(job.tasks.count())
    return sum(count_list)
