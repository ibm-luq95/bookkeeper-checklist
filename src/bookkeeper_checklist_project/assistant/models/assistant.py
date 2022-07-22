from client.models import Client
from company_services.models import CompanyService
from core.choices import AssistantTypeEnum, CustomUserStatusEnum
from core.models import BaseModelMixin
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _


class Assistant(BaseModelMixin):
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
        related_name="assistant",
    )
    assistant_type = models.CharField(
        _("assistant_type"),
        max_length=15,
        choices=AssistantTypeEnum.choices,
        default=AssistantTypeEnum.ALL,
    )
    company_services = models.ForeignKey(
        to=CompanyService, on_delete=models.PROTECT, null=True, related_name="assistant"
    )
    clients = models.ManyToManyField(to=Client)

    class Meta(BaseModelMixin.Meta):
        permissions = [
            ("can_access_bookkeeper", _("Can access bookkeeper account details")),
            ("can_edit_bookkeeper", _("Can edit bookkeeper account details")),
            ("can_access_client", _("Can access client(s) account details")),
        ]
