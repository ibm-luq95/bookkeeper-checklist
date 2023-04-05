import textwrap
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone
from django.utils.translation import gettext as _

from core.choices import StatusEnum
from core.constants.general import DEFAULT_SHORT_TRUNCATED_STRING
from core.models import SoftDeleteManager
from core.utils import sort_dict
from core.utils.developments.debugging_print import debugging_print


class DiffingMixin:
    def __init__(self, *args, **kwargs):
        super(DiffingMixin, self).__init__(*args, **kwargs)
        self._original_state = dict(self.__dict__)

    def get_changed_columns(self) -> dict:
        missing = object()
        result = {}
        for key, value in self._original_state.items():
            if key != self.__dict__.get(key, missing):
                result[key] = value
        return result


class BaseModelMixin(DiffingMixin, models.Model):
    # this will use in get_fields_as_list, and will use in serializers fields attribute
    EXCLUDED_FIELDS = (
        "id",
        "metadata",
        "is_deleted",
        "updated_at",
        "created_at",
        "deleted_at",
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    metadata = models.JSONField(_("metadata"), null=True, blank=True, default=dict)
    is_deleted = models.BooleanField(_("is_deleted"), default=False)
    created_at = models.DateTimeField(
        _("created_at"), default=timezone.now, editable=False
    )
    updated_at = models.DateTimeField(
        _("updated_at"), auto_now=True, blank=True, null=True, editable=False
    )
    deleted_at = models.DateTimeField(_("deleted_at"), null=True, default=None, blank=True)

    objects = SoftDeleteManager()
    # objects = models.Manager()
    original_objects = models.Manager()

    class Meta:
        abstract = True
        # ordering = ["-created_at", "-updated_at"]
        ordering = ["-created_at"]
        permissions = [
            ("can_view_list", "Can view list view"),
            ("view_archive", "Can view archive"),
        ]

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

    @property
    # @classmethod
    def get_fields_as_list(self) -> list:
        fields_list = []
        debugging_print(self)
        # for field in self._meta.get_fields(include_parents=False):
        #     debugging_print(field)
        # debugging_print(self._meta.fields)
        keys_list = list(self.get_instance_as_dict.keys())
        for item in keys_list:
            if item not in BaseModelMixin.EXCLUDED_FIELDS:
                fields_list.append(item)
        return fields_list


class UserForeignKeyMixin(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(class)s_related",
    )

    class Meta:
        abstract = True


class CreatedByMixin(models.Model):
    created_by = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False,
    )

    class Meta:
        abstract = True


class GetObjectSectionMixin(models.Model):
    class Meta:
        abstract = True

    def get_object_section(self):
        if self.job:
            return self.job
        elif self.client:
            return self.client
        elif self.task:
            return self.task


class StartAndDueDateMixin(models.Model):
    start_date = models.DateField(
        _("start date"), default=timezone.now, null=True, blank=True
    )
    due_date = models.DateField(_("due date"), default=timezone.now, null=True, blank=True)

    class Meta:
        abstract = True


class StartDateOnlyMixin(models.Model):
    start_date = models.DateField(
        _("start date"), default=timezone.now, null=True, blank=True
    )

    class Meta:
        abstract = True


class DueDateOnlyMixin(models.Model):
    due_date = models.DateField(_("due date"), default=timezone.now, null=True, blank=True)

    class Meta:
        abstract = True


class StrModelMixin(models.Model):
    def __str__(self) -> str:
        if hasattr(self, "title"):
            return textwrap.shorten(
                self.title, width=DEFAULT_SHORT_TRUNCATED_STRING, placeholder="..."
            )
            # return self.title
        elif hasattr(self, "body"):
            return textwrap.shorten(
                self.body, width=DEFAULT_SHORT_TRUNCATED_STRING, placeholder="..."
            )
        elif hasattr(self, "name"):
            return textwrap.shorten(
                self.name, width=DEFAULT_SHORT_TRUNCATED_STRING, placeholder="..."
            )

    class Meta:
        abstract = True


class GeneralStatusFieldMixin(models.Model):
    status = models.CharField(
        _("status"), max_length=10, choices=StatusEnum.choices, default=StatusEnum.ENABLED
    )

    class Meta:
        abstract = True
