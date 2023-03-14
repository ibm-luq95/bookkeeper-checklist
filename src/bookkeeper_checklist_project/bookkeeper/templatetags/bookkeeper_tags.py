# -*- coding: utf-8 -*-#
from django import template
from django.db.models import Q

from bookkeeper.models import Bookkeeper, BookkeeperProxy
from client.models import Client
from core.models import BaseQuerySetMixin

register = template.Library()


@register.filter(name="get_jobs_by_status")
def get_jobs_by_status(client: Client, job_status: str) -> BaseQuerySetMixin:
    jobs = client.jobs.filter(status=job_status).select_related()
    return jobs


@register.filter(name="get_jobs_by_type")
def get_jobs_by_type(client: Client, job_type: str) -> BaseQuerySetMixin:
    query_filter = None
    if job_type == "all":
        query_filter = ~Q(job_type__in=["weekly", "monthly", "quarterly", "yearly"])
    else:
        query_filter = Q(job_type__in=[job_type])

    jobs = client.jobs.filter(query_filter).select_related()
    return jobs


@register.filter(name="get_clients_for_bookkeeper_proxy")
def get_clients_for_bookkeeper_proxy(bookkeeper: Bookkeeper) -> BaseQuerySetMixin:
    return BookkeeperProxy.objects.get(pk=bookkeeper.pk).clients.all()


@register.filter(name="get_tasks_for_bookkeeper_proxy")
def get_tasks_for_bookkeeper_proxy(bookkeeper: Bookkeeper) -> BaseQuerySetMixin | None:
    bookkeeper_proxy = BookkeeperProxy.objects.get(pk=bookkeeper.pk)
    return bookkeeper_proxy.get_all_tasks_qs()
