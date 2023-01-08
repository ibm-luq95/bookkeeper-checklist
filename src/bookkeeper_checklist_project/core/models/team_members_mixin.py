# -*- coding: utf-8 -*-#
from django.db import models
import re

from assistant.models import Assistant
from bookkeeper.models import Bookkeeper
from manager.models import Manager
from core.utils import foreign_key_snake_case_plural


class CustomForeignKey(models.ForeignKey):
    def contribute_to_class(self, cls, name, private_only=False, **kwargs):
        super().contribute_to_class(cls, name, private_only=False, **kwargs)
        # self.remote_field.related_name = "_".join(re.findall("[A-Z][^A-Z]*", cls.__name__))
        self.remote_field.related_name = foreign_key_snake_case_plural(cls.__name__)


class TeamMembersMixin(models.Model):
    assistant = CustomForeignKey(
        to=Assistant,
        on_delete=models.PROTECT,
        related_name="%(class)s",
        null=True,
        blank=True,
    )
    bookkeeper = CustomForeignKey(
        to=Bookkeeper,
        on_delete=models.PROTECT,
        related_name="%(class)s",
        null=True,
        blank=True,
    )
    manager = CustomForeignKey(
        to=Manager,
        on_delete=models.PROTECT,
        related_name="%(class)s",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

    def get_managed_user(self):
        if self.bookkeeper:
            return self.bookkeeper
        elif self.assistant:
            return self.assistant
        elif self.manager:
            return self.manager
        else:
            return None

    @property
    def get_user_type(self):
        return self.get_managed_user().user.user_type
