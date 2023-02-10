# -*- coding: utf-8 -*-#

import traceback

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from core.utils import get_formatted_logger
from documents.forms import DocumentForm
from jobs.models import Job
from notes.forms import NoteForm
from task.forms import TaskForm
from .mixins import BookkeeperAccessMixin
from core.choices import JobStatusEnum

logger = get_formatted_logger(__file__)


class JobListView(LoginRequiredMixin, BookkeeperAccessMixin, ListView):
    login_url = reverse_lazy("users:auth:login")
    template_name = "bookkeeper/jobs/list.html"
    model = Job

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", "All Jobs")

        return context

    def get_queryset(self):
        try:
            bookkeeper = self.request.user.bookkeeper
            jobs_list = []
            jobs = Job.objects.all()
            for job in jobs:
                # check if the bookkeeper in the job bookkeepers
                if bookkeeper in job.bookkeeper.filter():
                    jobs_list.append(job.pk)
            jobs = Job.objects.select_related().filter(pk__in=jobs_list)
            return jobs
        except Exception as ex:
            logger.error(traceback.format_exc())
            raise Exception(str(ex))


class JobDetailView(
    LoginRequiredMixin, BookkeeperAccessMixin, UserPassesTestMixin, DetailView
):
    login_url = reverse_lazy("users:auth:login")
    template_name = "bookkeeper/jobs/detail.html"
    model = Job

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        job_object = self.get_object()
        document_form = DocumentForm(document_section="job", client=job_object.client)
        task_form = TaskForm(client=job_object.client, job=job_object)
        note_form = NoteForm(client=job_object.client, note_section="job")
        context["title"] = f"Job - {job_object.title}"
        context.setdefault("task_form", task_form)
        context.setdefault("document_form", document_form)
        context.setdefault("note_form", note_form)
        context.setdefault("title", f"Job - {job_object.title}")
        context.setdefault("job_status", JobStatusEnum.choices)

        return context

    def test_func(self) -> bool | None:
        job = self.get_object()
        bookkeepers_list = []
        bookkeeper = self.request.user.bookkeeper
        for book_keeper in job.bookkeeper.filter():
            bookkeepers_list.append(book_keeper)
        if bookkeeper in bookkeepers_list:
            return True
        else:
            return False
