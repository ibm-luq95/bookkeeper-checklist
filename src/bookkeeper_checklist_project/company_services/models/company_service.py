from core.choices import ServiceNameEnum
from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class CompanyService(BaseModelMixin):
    """This represents the company services

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    label = models.CharField(_("label"), max_length=30, null=True)
    service_name = models.CharField(
        _("service_name"), max_length=35, choices=ServiceNameEnum.choices
    )
    email = models.EmailField(_("email"), max_length=60, null=False)
    password = models.CharField(_("password"), max_length=250, null=False)
