from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class TaskItem(BaseModelMixin):
    title = models.CharField(_("title"), max_length=80, null=True)
    is_completed = models.BooleanField(_("is_completed"), default=False)
    hints = models.CharField(_("hints"), max_length=50, null=True, blank=True)
