import uuid


from core.utils import sort_dict
from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone
from django.utils.translation import gettext as _


class BaseModelMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    metadata = models.JSONField(_("metadata"), default=dict, null=True)
    created_at = models.DateTimeField(
        _("created_at"), default=timezone.now, editable=False
    )
    updated_at = models.DateTimeField(
        _("updated_at"), auto_now=True, blank=True, null=True
    )

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]

    @property
    def get_instance_as_dict(self) -> dict:
        return sort_dict(model_to_dict(self))
