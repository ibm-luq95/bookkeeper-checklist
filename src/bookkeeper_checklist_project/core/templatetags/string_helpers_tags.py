# -*- coding: utf-8 -*-#
import stringcase
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="to_title_case")
@stringfilter
def to_title_case(text) -> str:
    return stringcase.titlecase(text)
