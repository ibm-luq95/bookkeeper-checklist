from core.choices import ServiceNameEnum
from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _
from client.models import Client


class CompanyService(BaseModelMixin):
    """This represents the company services

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    client = models.ForeignKey(
        to=Client,
        on_delete=models.PROTECT,
        null=True,
        related_name="company_services",
    )
    service_name = models.CharField(
        _("service name"), max_length=35, choices=ServiceNameEnum.choices
    )
    label = models.CharField(_("label"), max_length=30, null=True)
    url = models.URLField(_("URL"), null=True, blank=True)
    email = models.EmailField(_("email"), max_length=60, null=False)
    password = models.CharField(_("password"), max_length=250, null=False)
