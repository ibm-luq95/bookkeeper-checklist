# -*- coding: utf-8 -*-#
from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class Task(BaseModelMixin):
    """Tasks for every job

    Args:
        BaseModelMixin (models.Model): The base django model mixin
    """    
    title = models.CharField(_("title"), max_length=80, null=True)
    is_completed = models.BooleanField(_("is_completed"), default=False)
    hints = models.CharField(_("hints"), max_length=50, null=True, blank=True)
    due_date = models.DateField(_("due_date"))

