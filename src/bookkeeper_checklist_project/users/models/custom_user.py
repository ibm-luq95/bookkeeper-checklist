from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _

from core.choices import CustomUserTypeEnum, CustomUserStatusEnum, UserTypesEnum
from core.models.mixins import BaseModelMixin
from core.utils import get_formatted_logger
from .manager import CustomUserManager

# TODO: remove the custom logger before push (only for development)
# ###### [Custom Logger] #########
logger = get_formatted_logger()


# ###### [Custom Logger] #########


class CustomUser(BaseModelMixin, AbstractBaseUser, PermissionsMixin):
    """Custom user model, it used instead of default django user model

    Args:
        AbstractBaseUser (_type_): _description_
        PermissionsMixin (_type_): _description_

    Returns:
        _type_: _description_
    """

    first_name = models.CharField(_("first name"), max_length=15)
    last_name = models.CharField(_("last name"), max_length=15)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(_("is_staff"), default=False)
    is_active = models.BooleanField(_("is_active"), default=True)
    date_joined = models.DateTimeField(_("date_joined"), default=timezone.now)
    user_type = models.CharField(
        _("user type"), choices=CustomUserTypeEnum.choices, max_length=15
    )
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=CustomUserStatusEnum.choices,
        default=CustomUserStatusEnum.ENABLED,
    )
    user_genre = models.CharField(
        _("user genre"),
        max_length=10,
        choices=UserTypesEnum.choices,
        default=UserTypesEnum.USER,
        db_index=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["-created_at", "-updated_at"]
        permissions = [
            ("developer_user", "Developer User"),
        ]

    def __str__(self):
        # return self.email
        # full_info = f"{self.fullname}:-> {self.user_type}"
        # full_info = f"{self.user_type.title()} - {self.fullname}"
        full_info = self.fullname
        return full_info

    # def get_absolute_url(self):
    #     return reverse("manager:users:detail", kwargs={"pk": self.pk})

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
