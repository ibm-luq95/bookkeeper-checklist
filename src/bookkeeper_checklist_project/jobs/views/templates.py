# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt
from core.views.mixins import BaseLoginRequiredMixin, BaseListViewMixin
from jobs.filters import JobTemplateFilter
from jobs.forms import JobTemplateForm
from manager.views.mixins import ManagerAssistantAccessMixin
from jobs.models import JobTemplate


class JobTemplateDetailsView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    DetailView,
):
    permission_required = "jobtemplate.view_jobtemplate"
    template_name = "jobs/templates/details.html"
    model = JobTemplate

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "Job Template Details")
        return context


class JobTemplatesListView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    BaseListViewMixin,
    ListView,
):
    permission_required = "jobtemplate.can_view_list"
    template_name = "jobs/templates/list.html"
    model = JobTemplate
    list_type = "list"
    paginate_by = LIST_VIEW_PAGINATE_BY

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("All jobs templates"))
        context.update({"app_label": "job_template"})
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "jobs templates".title())

        context.setdefault("filter_form", self.filterset.form)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = JobTemplateFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class JobTemplateUpdateView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = JobTemplate
    permission_required = "jobtemplate.change_jobtemplate"
    template_name = "jobs/templates/update.html"
    form_class = JobTemplateForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Job template updated successfully")
    success_url = reverse_lazy("jobs:templates:list")


class JobTemplateFactoryView(
    BaseLoginRequiredMixin,
    PermissionRequiredMixin,
    ManagerAssistantAccessMixin,
    SuccessMessageMixin,
    CreateView,
):
    model = JobTemplate
    permission_required = "jobtemplate.add_jobtemplate"
    template_name = "jobs/templates/factory.html"
    form_class = JobTemplateForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Job template created successfully")
    success_url = reverse_lazy("jobs:templates:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create job template"))
        return context

    def get_form_kwargs(self):
        kwargs = super(JobTemplateFactoryView, self).get_form_kwargs()
        kwargs.update({"created_by": self.request.user})
        return kwargs
