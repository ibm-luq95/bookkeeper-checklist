# -*- coding: utf-8 -*-#
from django import template

from bookkeeper.models import Bookkeeper, BookkeeperProxy
from core.models import BaseQuerySetMixin

register = template.Library()


# @register.filter(name="get_tasks_for_bookkeeper_proxy")
# def get_tasks_for_bookkeeper_proxy(bookkeeper: Bookkeeper) -> BaseQuerySetMixin:
#     bookkeeper_proxy = BookkeeperProxy.objects.get(pk=bookkeeper.pk)
