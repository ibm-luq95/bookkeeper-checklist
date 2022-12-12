# -*- coding: utf-8 -*-#

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.contrib import messages

from core.utils import get_formatted_logger
from task.forms import TaskForm
from task.models import Task
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

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        bookkeeper = self.request.user.bookkeeper_related.get()
        tasks_list = []
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            # queryset = self.model._default_manager.all()  # Default
            for job in bookkeeper.jobs.all():
                # debugging_print(f"Job {job.title}")
                job_tasks = job.tasks.select_related().filter()
                # debugging_print(job_tasks)
                if job_tasks:
                    # debugging_print(job_tasks.count())
                    for task in job_tasks:
                        # debugging_print(dir(task.pk))
                        tasks_list.append(task.pk)
            queryset = Task.objects.prefetch_related().filter(pk__in=tasks_list)
        else:
            # debugging_print("IN ELSE")
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {"cls": self.__class__.__name__}
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset


class TaskUpdateView(
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
        return kwargs

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        start_date = form.cleaned_data.get("start_date")
        due_date = form.cleaned_data.get("due_date")
        if start_date > due_date:
            messages.error(self.request, "Error while update task!")
            form.add_error("start_date", "Due date must occur after start date")
            return super().form_invalid(form)
        self.object = form.save()
        return super().form_valid(form)
