# -*- coding: utf-8 -*-#
from django.db import models
from core.models import BaseQuerySetMixin
from core.utils import debugging_print


class SoftDeleteManager(models.Manager):

    def get_queryset(self) -> models.QuerySet:
        queryset = BaseQuerySetMixin(self.model, using=self._db).filter(is_deleted=False)
        # debugging_print(str(queryset.query))
        # print("########################")
        return queryset
