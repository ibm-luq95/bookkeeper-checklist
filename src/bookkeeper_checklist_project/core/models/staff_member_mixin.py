# -*- coding: utf-8 -*-#
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.utils.translation import gettext as _

from company_services.models import CompanyService
from core.choices import CustomUserStatusEnum
from core.constants.status_labels import CON_ARCHIVED
from core.models import SoftDeleteManager, BaseQuerySetMixin
from core.utils import get_trans_txt


class StaffMemberMixin(models.Model):
    user = models.OneToOneField(
        to=get_user_model(), on_delete=models.CASCADE, related_name="%(class)s"
    )
    slug = models.SlugField(
        _("slug"), max_length=250, null=True, blank=True, editable=False
    )
    profile_picture = models.ImageField(
        _("profile picture"), upload_to="profile_pictures/", null=True, blank=True
    )
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=CustomUserStatusEnum.choices,
        default=CustomUserStatusEnum.ENABLED,
    )
    company_services = models.ForeignKey(
        to=CompanyService,
        on_delete=models.PROTECT,
        null=True,
        related_name="%(class)s",
    )
    bio = models.TextField(_("bio"), null=True, blank=True)

    # objects = SoftDeleteManager()

    class Meta:
        # db_table = "staff_member"
        abstract = True

    # @classmethod
    # def __init_subclass__(cls, **kwargs):
    #     super().__init_subclass__(**kwargs)
    #     models.signals.post_save.connect(create_groups, sender=cls)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.fullname)
        super(StaffMemberMixin, self).save(*args, **kwargs)

    @property
    def is_active_labeled(self) -> str:
        if self.user.is_active is True:
            return get_trans_txt("Active")
        else:
            return get_trans_txt("Deactivate")

    def get_not_seen_special_assignments(self):
        return self.special_assignments.filter(
            Q(is_seen=False) & ~Q(status__in=[CON_ARCHIVED])
        )

    def get_user_jobs(self) -> BaseQuerySetMixin:
        if hasattr(self, "jobs"):
            return self.jobs.all()
