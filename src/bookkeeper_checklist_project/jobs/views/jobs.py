# -*- coding: utf-8 -*-#
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from core.choices import JobStatusEnum
from core.constants import LIST_VIEW_PAGINATE_BY
from core.utils import get_trans_txt
from core.views.mixins import BaseListViewMixin, BaseLoginRequiredMixin
from documents.forms import DocumentForm
from jobs.filters import JobFilter
from jobs.forms import JobForm
from jobs.models import Job
from manager.views.mixins import ManagerAccessMixin
from notes.forms import NoteForm
from special_assignment.forms import DiscussionForm
from task.forms import TaskForm


class JobListView(BaseLoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, ListView):
    template_name = "jobs/list.html"
    model = Job
    queryset = (
        Job.objects.select_related()
        .filter(~Q(status__in=["archive", "complete"]))
        .order_by("-created_at")
    )
    list_type = "list"
    paginate_by = LIST_VIEW_PAGINATE_BY

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("All jobs"))
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "jobs".title())

        context.setdefault("filter_form", self.filterset.form)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = JobFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class JobCreateView(
    BaseLoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, CreateView
):
    model = Job
    template_name = "jobs/create.html"
    form_class = JobForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Job created successfully")
    success_url = reverse_lazy("jobs:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "Create job")
        return context

    def get_form_kwargs(self):
        kwargs = super(JobCreateView, self).get_form_kwargs()
        kwargs.update({"created_by": self.request.user})
        return kwargs


class JobDetailsView(BaseLoginRequiredMixin, ManagerAccessMixin, DetailView):
    template_name = "jobs/details.html"
    model = Job

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        job_object = self.get_object()
        discussion_form = DiscussionForm(job=job_object)
        document_form = DocumentForm(document_section="job", client=job_object.client)
        task_form = TaskForm(client=job_object.client, job=job_object)
        note_form = NoteForm(client=job_object.client, note_section="job")
        context.setdefault("job_status", JobStatusEnum.choices)
        context.setdefault("title", f"Job - {job_object.title}")
        context.setdefault("task_form", task_form)
        context.setdefault("document_form", document_form)
        context.setdefault("note_form", note_form)
        context.setdefault("discussion_form", discussion_form)
        return context


class JobUpdateView(
    BaseLoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, UpdateView
):
    # model = get_user_model()
    template_name = "jobs/update.html"
    form_class = JobForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Job updated successfully")
    model = Job
    success_url = reverse_lazy("jobs:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Update Job"))
        return context

    def get_form_kwargs(self):
        kwargs = super(JobUpdateView, self).get_form_kwargs()
        kwargs.update({"is_updated": True})
        return kwargs


class JobDeleteView(
    BaseLoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, DeleteView
):
    model = Job
    template_name = "jobs/delete.html"
    # form_class = JobForm
    # http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Job deleted successfully")
    success_url = reverse_lazy("jobs:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Delete job")
        return context


class JobArchiveListView(
    BaseLoginRequiredMixin, ManagerAccessMixin, BaseListViewMixin, ListView
):
    template_name = "jobs/list.html"
    model = Job
    queryset = (
        Job.objects.select_related()
        .filter(Q(status__in=["archive", "complete"]))
        .order_by("-created_at")
    )
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "archive"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Archived jobs".title()))
        context.setdefault("page_header", get_trans_txt("archived jobs".title()))
        context.setdefault("list_type", self.list_type)
        return context
