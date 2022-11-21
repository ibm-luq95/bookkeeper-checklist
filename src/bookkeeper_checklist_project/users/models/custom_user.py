import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.forms.models import model_to_dict
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _

from core.choices import CustomUserTypeEnum
from core.utils import get_formatted_logger
from core.utils import sort_dict
from .manager import CustomUserManager

# TODO: remove the custom logger before push (only for development)
# ###### [Custom Logger] #########
logger = get_formatted_logger(__name__)
# ###### [Custom Logger] #########


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model, it used instead of default django user model

    Args:
        AbstractBaseUser (_type_): _description_
        PermissionsMixin (_type_): _description_

    Returns:
        _type_: _description_
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_("first name"), max_length=15)
    last_name = models.CharField(_("last name"), max_length=15)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(_("is_staff"), default=False)
    is_active = models.BooleanField(_("is_active"), default=True)
    date_joined = models.DateTimeField(_("date_joined"), default=timezone.now)
    user_type = models.CharField(
        _("user type"), choices=CustomUserTypeEnum.choices, max_length=15
    )
    metadata = models.JSONField(
        _("metadata"),
        null=True,
        blank=True,
        default=dict,
        help_text="Enter as JSON object",
    )
    is_deleted = models.BooleanField(_("is_deleted"), default=False)
    created_at = models.DateTimeField(_("created_at"), default=timezone.now, editable=False)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        # return self.email
        full_info = f"{self.fullname}:-> {self.email}"
        return full_info

    def get_absolute_url(self):
        return reverse("manager:users:detail", kwargs={"pk": self.pk})

    @property
    def get_instance_as_dict(self) -> dict:
        data = model_to_dict(self)
        data.setdefault("id", self.id)
        data.setdefault("created_at", self.created_at)
        return sort_dict(data)

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
