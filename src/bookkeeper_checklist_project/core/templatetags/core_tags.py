# -*- coding: utf-8 -*-#
from django import template
from django.core.paginator import Paginator

from core.constants import LIST_VIEW_PAGINATE_BY

register = template.Library()


@register.filter(name="get_paginator_object")
def get_paginator_object(objects_list) -> Paginator:
    return Paginator(objects_list, 1)
