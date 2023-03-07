from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModelMixin, StaffMemberMixin


class Bookkeeper(BaseModelMixin, StaffMemberMixin):
    """Bookkeeper model

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    class Meta:
        # proxy = True
        permissions = [
            ("bookkeeper_user", "Bookkeeper User"),
        ]

    def __str__(self):
        # return f"Bookkeeper -> {self.user.fullname}"
        return f"{self.user.fullname}"


def get_all_bookkeepers_as_choices() -> list:
    all_bookkeepers = []
    if Bookkeeper.objects.select_related().count() > 0:
        for bookkeeper in Bookkeeper.objects.select_related().all():
            all_bookkeepers.append((bookkeeper.pk, f"{bookkeeper.user.fullname}"))

    return all_bookkeepers
