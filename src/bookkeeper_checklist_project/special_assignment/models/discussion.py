# -*- coding: utf-8 -*-#
from typing import Union

from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModelMixin
from .special_assignment import SpecialAssignment
from manager.models import Manager


class Discussion(BaseModelMixin):
    special_assignment = models.ForeignKey(
        to=SpecialAssignment, on_delete=models.CASCADE, related_name="discussions"
    )
    body = models.TextField(_("body"))
    replies = models.ForeignKey(
        to="self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True
    )
