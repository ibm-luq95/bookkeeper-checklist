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


class DBBackupListView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    # ManagerAccessMixin,
    BaseListViewMixin,
    ListViewMixin,
    ListView,
):
    permission_required = "db_backup_restore.can_view_list"
    template_name = "db_backup_restore/db_backup/list.html"
    model = DBBackup
    list_type = "list"
    paginate_by = LIST_VIEW_PAGINATE_BY

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("All db backups"))
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "backups".title())

        # context.setdefault("filter_form", self.filterset.form)
        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = JobFilter(self.request.GET, queryset=queryset)
    #     return self.filterset.qs


class DBBackupCreateView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    model = DBBackup
    permission_required = "db_backup_restore.can_add"
    template_name = "db_backup_restore/db_backup/create.html"
    form_class = BackupForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("DB backup created successfully")
    success_url = reverse_lazy("db_backup_restore:backup:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "Create db backup")
        return context


class DBBackupDetailsView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView,
):
    template_name = "db_backup_restore/db_backup/details.html"
    model = DBBackup
    permission_required = "db_backup_restore.view_dbbackup"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", f"Backup - {self.get_object().name}")
        return context
