from django.db import models
from django.utils.translation import gettext as _
from core.models import BaseModelMixin


class ServiceNameEnum(models.TextChoices):
    OFFICE_365 = "office_365", _("Office 365")
    SUPPORT_SYSTEM = "support_system", _("Support System")
    FOCALBOARD = "focalboard", _("Focalboard System")
    PORTAL_SYSTEM = "portal_system", _("Portal System")
    BOOKKEEPER_CHECKLIST_APP = "bookkeeper_checklist_app", _("Bookkeeper Checklist App")
    QUICKBOOKS_ONLINE = "quickbooks_online", _("Quickbooks Online")
    MAILCHIMP = "mailchimp", _("Mailchimp")
    CRM = "crm", _("CRM")
    BLOG = "blog", _("Blog")
    KENNECTED = "kennected", _("Kennected")
    SHARED_ACCOUNTS = "shared_accounts", _("Shared Accounts")


class CompanyService(BaseModelMixin):
    label = models.CharField(_("label"), max_length=30, null=True)
    service_name = models.CharField(
        _("service_name"), max_length=20, choices=ServiceNameEnum.choices
    )
    email = models.EmailField(_("email"), max_length=60, null=False)
    password = models.CharField(_("password"), max_length=250, null=False)
