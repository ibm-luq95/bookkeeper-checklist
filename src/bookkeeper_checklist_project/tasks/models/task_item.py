from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class TaskItem(BaseModelMixin):
    title = models.CharField(_("title"), max_length=80, null=True)
