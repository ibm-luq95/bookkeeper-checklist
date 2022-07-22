from django.db import models
from django.utils.translation import gettext as _


class CustomUserStatusEnum(models.TextChoices):
    ENABLED = "enabled", _("Enabled")
    PENDING = "pending", _("Pending")
    CANCELED = "canceled", _("Canceled")
    DISABLED = "disabled", _("Disabled")


class AssistantTypeEnum(models.TextChoices):
    ALL = "all", _("All")
    MARKETING = "marketing", _("Marketing")
    ADMIN = "admin", _("Admin")
    BOOKKEEPING = "bookkeeping", _("Bookkeeping")


class AccountType(models.TextChoices):
    CHECKING_ACCOUNT = "checking_account", _("Checking Account")
    SAVING_ACCOUNT = "saving_account", _("Saving Account")
    CREDITCARD = "credit_card", _("CreditCard")
    LOAN = "loan", _("Loan")


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


class TaskTypeEnum(models.TextChoices):
    NO_TYPE = "no_type", _("No Type")
    RECURRING = "recurring", _("Recurring")
    WEEKLY = "weekly", _("Weekly")
    MONTHLY = "monthly", _("Monthly")
    QUARTERLY = "quarterly", _("Quarterly")
    YEARLY = "yearly", _("Yearly")
    ONE_TIME = "one_time", _("One Time")
    URGENT = "urgent", _("Urgent")


class TaskStatusEnum(models.TextChoices):
    NOT_STARTED = "not_started", _("Not Started")
    IN_PROGRESS = "in_progress", _("In progress")
    PAST_DUE = "past_due", _("Past Due")
    COMPLETE = "complete", _("Complete")


class CustomUserTypeEnum(models.TextChoices):
    BOOKKEEPER = "bookkeeper", _("Bookkeeper")
    ASSISTANT = "assistant", _("Assistant")
