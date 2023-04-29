# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from bookkeeper.models import BookkeeperProxy
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt
from core.views.mixins import BaseLoginRequiredMixin, BaseListViewMixin
from documents.forms import DocumentTemplateForm
from jobs.filters import JobTemplateFilter
from jobs.forms import JobTemplateForm, JobCategoryForm
from manager.views.mixins import ManagerAssistantAccessMixin, ManagerAccessMixin
from jobs.models import JobCategory
from notes.forms import NoteTemplateForm
from task.forms import TaskItemForm, TaskTemplateForm
from client.models import ClientProxy


class JobCategoryListView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    BaseListViewMixin,
    ListView,
):
    permission_required = "jobcategory.can_view_list"
    template_name = "jobs/category/list.html"
    model = JobCategory
    list_type = "list"
    paginate_by = LIST_VIEW_PAGINATE_BY

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Job categories"))
        context.update({"app_label": "jobs:category"})
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "jobs categories".title())

        return context


class JobCategoryCreateView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    CreateView,
):
    model = JobCategory
    permission_required = "jobcategory.add_jobcategory"
    template_name = "jobs/category/create.html"
    form_class = JobCategoryForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Job category created successfully")
    success_url = reverse_lazy("jobs:category:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create job category"))
        return context


class JobCategoryUpdateView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = JobCategory
    permission_required = "jobcategory.edit_jobcategory"
    template_name = "jobs/category/update.html"
    form_class = JobCategoryForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Job category updated successfully")
    success_url = reverse_lazy("jobs:category:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update job category"))
        return context


class JobCategoryDeleteView(
    BaseLoginRequiredMixin,
    ManagerAccessMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "jobcategory.delete_jobcategory"
    model = JobCategory
    success_message = get_trans_txt("Category deleted successfully")
    template_name = "jobs/category/delete.html"
    success_url = reverse_lazy("jobs:category:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("delete category".capitalize()))
        return context
