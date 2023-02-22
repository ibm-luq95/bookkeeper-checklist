# -*- coding: utf-8 -*-#
from django.db import models
from django.db.models import Q

from core.constants.status_labels import CON_COMPLETED, CON_ARCHIVED
from core.models import BaseQuerySetMixin


class SoftDeleteManager(models.Manager):
    def get_queryset(self) -> BaseQuerySetMixin:
        # check if it is task model or not
        if hasattr(self.model, "task_status") is True:
            queryset = BaseQuerySetMixin(self.model, using=self._db).filter(
                ~Q(task_status__in=[CON_COMPLETED, CON_ARCHIVED]), Q(is_deleted=False)
            )
        elif hasattr(self.model, "status") is True:
            queryset = BaseQuerySetMixin(self.model, using=self._db).filter(
                Q(is_deleted=False),
                ~Q(status__in=[CON_COMPLETED, CON_ARCHIVED]),
            )
        else:
            queryset = BaseQuerySetMixin(self.model, using=self._db).filter(
                Q(is_deleted=False)
            )

        return queryset
