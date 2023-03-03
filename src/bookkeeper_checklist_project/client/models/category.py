# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModelMixin


class ClientCategory(BaseModelMixin):
    name = models.CharField(_("name"), max_length=50)
