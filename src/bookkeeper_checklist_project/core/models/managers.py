# -*- coding: utf-8 -*-#
from django.db import models
from django.db.models import Q

from core.constants.status_labels import CON_COMPLETED, CON_ARCHIVED
from core.models import BaseQuerySetMixin


class SoftDeleteManager(models.Manager):
    def get_queryset(self) -> BaseQuerySetMixin:
        queryset = BaseQuerySetMixin(self.model, using=self._db).filter(
            Q(is_deleted=False)
        )

        return queryset
