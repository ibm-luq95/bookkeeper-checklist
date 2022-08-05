from core.choices import CustomUserTypeEnum
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first_name"), max_length=15)
    last_name = models.CharField(_("last_name"), max_length=15)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(_("is_staff"), default=False)
    is_active = models.BooleanField(_("is_active"), default=True)
    date_joined = models.DateTimeField(_("date_joined"), default=timezone.now)
    user_type = models.CharField(
        _("user type"), choices=CustomUserTypeEnum.choices, max_length=15
    )
    metadata = models.JSONField(_("metadata"), default=dict, null=True)
    created_at = models.DateTimeField(
        _("created_at"), default=timezone.now, editable=False
    )
    updated_at = models.DateTimeField(
        _("updated_at"), auto_now=True, blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
