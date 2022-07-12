from client.models import Client
from company_services.models import CompanyService
from core.models import StaffModelMixin
from django.db import models
from django.utils.translation import gettext as _


class AssistantTypeEnum(models.TextChoices):
    ALL = "all", _("All")
    MARKETING = "marketing", _("Marketing")
    ADMIN = "admin", _("Admin")
    BOOKKEEPING = "bookkeeping", _("Bookkeeping")


class Assistant(StaffModelMixin):
    assistant_type = models.CharField(
        _("assistant_type"),
        max_length=15,
        choices=AssistantTypeEnum.choices,
        default=AssistantTypeEnum.ALL,
    )
