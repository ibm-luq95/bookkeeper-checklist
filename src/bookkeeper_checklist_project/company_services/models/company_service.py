# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from client.models import ClientProxy
from company_services.helpers import PasswordHasher
from core.choices import ServiceNameEnum
from core.models import BaseModelMixin, CreatedByMixin, GeneralStatusFieldMixin


class CompanyService(BaseModelMixin, GeneralStatusFieldMixin, CreatedByMixin):
    """This represents the company services

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    client = models.ForeignKey(
        to=ClientProxy,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="company_services",
        db_index=True,
    )
    service_name = models.CharField(
        _("service name"), max_length=35, choices=ServiceNameEnum.choices, db_index=True
    )
    label = models.CharField(_("label"), max_length=30, null=True)
    url = models.URLField(_("URL"), null=True, blank=True)
    username = models.CharField(
        _("username"), max_length=100, null=False, db_index=True, default=None, blank=False
    )
    password = models.TextField(_("password"), null=True, blank=True)

    def __str__(self):
        return f"Service for {self.client.name}, labeled: {self.label}"

    # def save(self, *args, **kwargs):
    #     self.password = PasswordHasher.encrypt(self.password)
    #     super(CompanyService, self).save(*args, **kwargs)

    @property
    def decrypted_password(self) -> str | None:
        if not self.password:
            return None
        else:
            # debugging_print(self.password)
            return PasswordHasher.decrypt(self.password)
