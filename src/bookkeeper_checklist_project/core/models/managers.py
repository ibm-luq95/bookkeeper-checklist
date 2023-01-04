# -*- coding: utf-8 -*-#
from django.db import models

from core.models import BaseQuerySetMixin


class SoftDeleteManager(models.Manager):
    def get_queryset(self) -> BaseQuerySetMixin:
        queryset = BaseQuerySetMixin(self.model, using=self._db).filter(is_deleted=False)
        return queryset
