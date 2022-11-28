# -*- coding: utf-8 -*-#
from django import template

from client.models import Client
from core.models import BaseQuerySetMixin

register = template.Library()


@register.filter(name="get_jobs_by_status")
def get_jobs_by_status(client: Client, job_status: str) -> BaseQuerySetMixin:
    jobs = client.jobs.filter(status=job_status).select_related()
    return jobs


@register.filter(name="get_jobs_by_type")
def get_jobs_by_type(client: Client, job_type: str) -> BaseQuerySetMixin:
    jobs = client.jobs.filter(job_type=job_type).select_related()
    return jobs
