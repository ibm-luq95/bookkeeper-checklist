# -*- coding: utf-8 -*-#
import traceback

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from special_assignment.models import SpecialAssignment
from core.utils import get_formatted_logger, get_trans_txt, debugging_print
from special_assignment.forms import DiscussionForm
from jobs.models import Job
from .mixins import BookkeeperAccessMixin

logger = get_formatted_logger(__file__)


class SpecialAssignmentsListView(LoginRequiredMixin, BookkeeperAccessMixin, ListView):
    template_name = "bookkeeper/special_assignment/list.html"
    login_url = reverse_lazy("users:login")
    model = SpecialAssignment
    http_method_names = ["get"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("All special assignment"))
        bookkeeper = self.request.user.bookkeeper

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        bookkeeper = self.request.user.bookkeeper
        queryset = bookkeeper.special_assignments.select_related().all()
        return queryset


class SpecialAssignmentDetailsView(LoginRequiredMixin, BookkeeperAccessMixin, DetailView):
    login_url = reverse_lazy("users:login")
    template_name = "bookkeeper/special_assignment/details.html"
    model = SpecialAssignment

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        status = {
            "not_started": get_trans_txt("Not Started"),
            "in_progress": get_trans_txt("In Progress"),
            "completed": get_trans_txt("Completed"),
            "rejected": get_trans_txt("Rejected"),
        }
        special_assignment = self.get_object()
        context.setdefault("title", get_trans_txt(special_assignment.title))
        discussion_form = DiscussionForm(
            special_assignment=special_assignment, discussion_user=self.request.user
        )
        context.setdefault("status", status)
        context.setdefault("discussion_form", discussion_form)
        if special_assignment.is_seen is False:
            special_assignment_user = special_assignment.get_managed_user().user
            current_user = self.request.user
            if special_assignment_user == current_user:
                special_assignment.is_seen = True
                special_assignment.save()

        return context
