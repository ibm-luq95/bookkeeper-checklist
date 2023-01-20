# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from core.utils import get_trans_txt
from task.forms import TaskForm
from task.models import Task
from .mixins import ManagerAccessMixin


class TasksListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/task/list.html"
    model = Task
    queryset = Task.objects.select_related().filter(~Q(task_status="archive"))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("All tasks")
        return context


class TasksArchiveListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/task/archive_list.html"
    model = Task
    queryset = Task.objects.select_related().filter(Q(task_status="archive"))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("All tasks")
        return context


class TaskCreateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, CreateView
):
    model = Task
    template_name = "manager/task/create.html"
    form_class = TaskForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Task created successfully")
    success_url = reverse_lazy("manager:task:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Create task"))
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class TaskUpdateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, UpdateView
):
    # model = get_user_model()
    template_name = "manager/task/update.html"
    form_class = TaskForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Task updated successfully")
    model = Task

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Update Task")
        return context

    def get_success_url(self):
        task = self.get_object()
        url = reverse_lazy("manager:task:update", kwargs={"pk": task.pk})
        return url


class TaskDeleteView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, DeleteView
):
    login_url = reverse_lazy("users:login")
    model = Task
    template_name = "manager/task/delete.html"
    success_message: str = get_trans_txt("Task deleted successfully!")
    success_url = reverse_lazy("manager:task:list")
