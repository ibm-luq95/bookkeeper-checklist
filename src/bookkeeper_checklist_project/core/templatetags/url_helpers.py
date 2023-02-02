# -*- coding: utf-8 -*-#
from typing import Optional
from uuid import UUID

from django import template
from django.urls import reverse_lazy, NoReverseMatch

from prettyprinter import pprint

register = template.Library()


@register.filter(name="get_last_url_part")
def get_last_url_part(full_url: str) -> str:
    last_part = full_url.rsplit("/")[-1]
    return last_part


# @register.filter(name="get_url_path_by_name")
@register.simple_tag
def get_url_path_by_name(
    app_name: str,
    user_type: str,
    object_pk: Optional[UUID] = None,
    action: Optional[str] = None,
) -> str:
    # {% get_url_path_by_name app_name=app_name user_type=user_type object_pk=object_pk action_name='update' %}
    pprint(locals())
    # try:
    #     if app_name and user_type:
    #         app_pattern = f"{app_name}:{user_type}:{action_name}"
    #         if object_pk is not None:
    #             url_path = reverse_lazy(app_pattern, kwargs={"pk": object_pk})
    #         else:
    #             url_path = reverse_lazy(app_pattern)
    #
    #     return url_path
    # except NoReverseMatch:
    #     return ""
