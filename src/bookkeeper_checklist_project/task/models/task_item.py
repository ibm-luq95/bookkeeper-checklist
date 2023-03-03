# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModelMixin, StartAndDueDateMixin, StrModelMixin


class TaskItem(BaseModelMixin, StartAndDueDateMixin, StrModelMixin):
    title = models.CharField(_("title"), max_length=150)
