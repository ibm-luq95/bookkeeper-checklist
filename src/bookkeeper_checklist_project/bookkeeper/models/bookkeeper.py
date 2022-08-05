from client.models import Client
from company_services.models import CompanyService
from core.choices import CustomUserStatusEnum
from core.models import BaseModelMixin
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _


class Bookkeeper(BaseModelMixin):
    slug = models.SlugField(_("slug"), max_length=250, null=True)
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=CustomUserStatusEnum.choices,
        default=CustomUserStatusEnum.ENABLED,
    )
    user = models.OneToOneField(
        to=get_user_model(),
        null=True,
        on_delete=models.PROTECT,
        related_name="bookkeeper",
    )
    company_services = models.ForeignKey(
        to=CompanyService, on_delete=models.PROTECT, null=True, related_name="bookkeeper"
    )
    clients = models.ManyToManyField(to=Client)
    is_active = models.BooleanField(_("is_active"), default=True)
