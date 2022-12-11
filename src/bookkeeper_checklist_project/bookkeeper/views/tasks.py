# -*- coding: utf-8 -*-#
import traceback

import faker
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.base import TemplateView

from client.models import Client
from core.utils import get_formatted_logger, debugging_print
from task.models import Task
from task.forms import TaskForm
from jobs.models import Job
from .mixins import BookkeeperAccessMixin

logger = get_formatted_logger(__file__)


class TaskListView(LoginRequiredMixin, BookkeeperAccessMixin, ListView):
    template_name = "bookkeeper/tasks/list.html"
    login_url = reverse_lazy("users:login")
    model = Task

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "All Tasks")

        return context

    # def get_queryset(self):
    #     try:
    #         bookkeeper = self.request.user.bookkeeper_related.get()
    #         jobs = bookkeeper.jobs.all()
    #         queryset = jobs
    #         return queryset
    #     except Exception as ex:
    #         logger.error(traceback.format_exc())
    #         raise Exception(str(ex))


class TaskDetailView(
    LoginRequiredMixin, BookkeeperAccessMixin, SuccessMessageMixin, UpdateView
):
    template_name = "bookkeeper/tasks/details.html"
    login_url = reverse_lazy("users:login")
    model = Task
    form_class = TaskForm
    success_message = "Task Update Successfully"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        context.setdefault("title", f"Task - {task.title}")

        return context

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        if hasattr(self, "object"):
            kwargs.update({"instance": self.object})
        kwargs.update({"is_disable_job": True})
        debugging_print(kwargs)
        return kwargs
