# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from core.choices import JobStatusEnum
from core.utils import get_trans_txt
from jobs.forms import JobForm
from jobs.models import Job
from notes.forms import NoteForm
from special_assignment.forms import DiscussionForm
from task.forms import TaskForm
from documents.forms import DocumentForm
from .mixins import ManagerAccessMixin


class JobListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/jobs/list.html"
    model = Job
    queryset = (
        Job.objects.select_related()
        .filter(~Q(status__in=["archive", "complete"]))
        .order_by("-created_at")
    )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("All jobs")
        return context


class JobCreateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, CreateView
):
    model = Job
    template_name = "manager/jobs/create.html"
    form_class = JobForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Job created successfully")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Job"
        return context

    def get_form_kwargs(self):
        kwargs = super(JobCreateView, self).get_form_kwargs()
        kwargs.update({"created_by": self.request.user})
        return kwargs


class JobDetailsView(LoginRequiredMixin, ManagerAccessMixin, DetailView):
    template_name = "manager/jobs/details.html"
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
        context["title"] = f"Job - {job_object.title}"
        context.setdefault("task_form", task_form)
        context.setdefault("document_form", document_form)
        context.setdefault("note_form", note_form)
        context.setdefault("discussion_form", discussion_form)
        return context


class JobUpdateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, UpdateView
):
    # model = get_user_model()
    template_name = "manager/jobs/update.html"
    form_class = JobForm
    http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Job updated successfully")
    model = Job

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Update Job")
        return context


class JobDeleteView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, DeleteView
):
    model = Job
    template_name = "manager/jobs/delete.html"
    # form_class = JobForm
    # http_method_names = ["post", "get"]
    success_message: str = get_trans_txt("Job deleted successfully")
    success_url = reverse_lazy("manager:jobs:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Delete job")
        return context


class JobArchiveListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/jobs/archive_list.html"
    model = Job
    queryset = (
        Job.objects.select_related()
        .filter(Q(status__in=["archive", "complete"]))
        .order_by("-created_at")
    )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "All jobs"
        return context
