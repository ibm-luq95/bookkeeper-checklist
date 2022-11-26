import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone
from django.utils.translation import gettext as _

from core.models import SoftDeleteManager
from core.utils import sort_dict


class BaseModelMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    metadata = models.JSONField(_("metadata"), null=True, blank=True, default=dict)
    is_deleted = models.BooleanField(_("is_deleted"), default=False)
    created_at = models.DateTimeField(_("created_at"), default=timezone.now, editable=False)
    updated_at = models.DateTimeField(
        _("updated_at"), auto_now=True, blank=True, null=True, editable=False
    )
    deleted_at = models.DateTimeField(_("deleted_at"), null=True, default=None, blank=True)

    # undeleted_objects = SoftDeleteManager()
    # objects = models.Manager()
    objects = SoftDeleteManager()
    original_objects = models.Manager()

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    @property
    def get_instance_as_dict(self) -> dict:
        data = model_to_dict(self)
        data.setdefault("id", self.id)
        data.setdefault("created_at", self.created_at)
        data.setdefault("updated_at", self.updated_at)
        return sort_dict(data)


class UserForeignKeyMixin(models.Model):
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        abstract = True
