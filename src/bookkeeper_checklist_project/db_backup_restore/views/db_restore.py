# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.status_labels import CON_COMPLETED, CON_ARCHIVED
from core.utils import get_trans_txt, debugging_print
from core.views.mixins import (
    BaseListViewMixin,
    BaseLoginRequiredMixin,
    DetailsViewMixin,
    ListViewMixin,
    ArchiveListViewMixin,
)
from db_backup_restore.forms import BackupForm
from db_backup_restore.models import DBBackup
from manager.views.mixins import ManagerAccessMixin


class RestoreDBDetailsView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView,
):
    template_name = "db_backup_restore/restore/restoring.html"
    model = DBBackup
    permission_required = "db_backup_restore.view_dbbackup"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", f"Restore - {self.get_object().name}")
        return context
