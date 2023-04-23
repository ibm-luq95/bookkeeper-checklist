# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from bookkeeper.models import BookkeeperProxy
from core.utils import get_trans_txt, debugging_print
from core.views.mixins import (
    BaseListViewMixin,
    BaseLoginRequiredMixin,
    ListViewMixin,
    ArchiveListViewMixin,
)
from task.forms import TaskForm
from task.models import Task
from core.constants import LIST_VIEW_PAGINATE_BY
from manager.views.mixins import ManagerAccessMixin, ManagerAssistantAccessMixin
from task.filters import TaskFilter


class TasksListView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    BaseListViewMixin,
    ListViewMixin,
    ListView,
):
    permission_required = "task.can_view_list"
    template_name = "task/list.html"
    model = Task
    # queryset = Task.objects.select_related().filter(
    #     ~Q(task_status__in=[CON_ARCHIVED, CON_COMPLETED])
    # )
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Tasks"))
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", get_trans_txt("tasks".title()))
        context.setdefault("filter_form", self.filterset.form)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.user_type == "bookkeeper":
            queryset = BookkeeperProxy.objects.get(
                pk=self.request.user.bookkeeper.pk
            ).get_all_tasks_qs()
        self.filterset = TaskFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class TasksArchiveListView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    BaseListViewMixin,
    ArchiveListViewMixin,
    ListView,
):
    permission_required = "task.can_view_archive"
    template_name = "task/list.html"
    model = Task
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "archive"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("title", get_trans_txt("Archived tasks"))
        context.setdefault("page_header", get_trans_txt("archived tasks".title()))
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TaskFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class TaskCreateView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    permission_required = "task.add_task"
    # model = Task
    template_name = "task/create.html"
    form_class = TaskForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Task created successfully")
    success_url = reverse_lazy("task:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create task"))
        return context

    def get_form_kwargs(self):
        kwargs = super(TaskCreateView, self).get_form_kwargs()
        kwargs.update({"created_by": self.request.user})
        kwargs.update({"add_jodit_css_class": True})
        return kwargs


class TaskUpdateView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    permission_required = "task.change_task"
    # model = get_user_model()
    template_name = "task/update.html"
    form_class = TaskForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Task updated successfully")
    model = Task

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update Task"))
        debugging_print(self.get_object().status)
        return context

    def get_success_url(self):
        task = self.get_object()
        url = reverse_lazy("task:update", kwargs={"pk": task.pk})
        return url

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(TaskUpdateView, self).get_form_kwargs()
        kwargs.update({"add_jodit_css_class": True})
        return kwargs


class TaskDeleteView(
    BaseLoginRequiredMixin,
    ManagerAssistantAccessMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    permission_required = "task.delete_task"
    model = Task
    template_name = "task/delete.html"
    success_message: str = get_trans_txt("Task deleted successfully!")
    success_url = reverse_lazy("task:list")
