# -*- coding: utf-8 -*-#

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core.utils import get_formatted_logger, get_trans_txt
from special_assignment.forms import DiscussionForm, SpecialAssignmentForm
from special_assignment.models import SpecialAssignment
from .mixins import BookkeeperAccessMixin

logger = get_formatted_logger(__file__)


class SpecialAssignmentsListView(LoginRequiredMixin, BookkeeperAccessMixin, ListView):
    template_name = "bookkeeper/special_assignment/list.html"
    login_url = reverse_lazy("users:auth:login")
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
    login_url = reverse_lazy("users:auth:login")
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


class SpecialAssignmentCreateView(
    LoginRequiredMixin, BookkeeperAccessMixin, SuccessMessageMixin, CreateView
):
    login_url = reverse_lazy("users:auth:login")
    template_name = "bookkeeper/special_assignment/create.html"
    form_class = SpecialAssignmentForm
    success_message = get_trans_txt("Special assignment created successfully!")
    model = SpecialAssignment
    success_url = reverse_lazy("bookkeeper:special_assignment:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Create special assignment")
        return context

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({"assigned_by": self.request.user})
        return kwargs

    def form_valid(self, form):
        start_date = form.cleaned_data.get("start_date")
        due_date = form.cleaned_data.get("due_date")
        if start_date > due_date:
            form.add_error("start_date", get_trans_txt("Start date bigger than due date!"))
            return self.form_invalid(form)

        return super().form_valid(form)


class RequestedSpecialAssignmentsListView(
    LoginRequiredMixin, BookkeeperAccessMixin, ListView
):
    template_name = "bookkeeper/special_assignment/requested_assignments.html"
    login_url = reverse_lazy("users:auth:login")
    model = SpecialAssignment
    http_method_names = ["get"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("All requested special assignment"))
        bookkeeper = self.request.user.bookkeeper

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        bookkeeper = self.request.user.bookkeeper
        queryset = bookkeeper.user.requested_assignments.select_related().all()
        return queryset


class SpecialAssignmentUpdateView(
    LoginRequiredMixin, BookkeeperAccessMixin, SuccessMessageMixin, UpdateView
):
    login_url = reverse_lazy("users:auth:login")
    template_name = "bookkeeper/special_assignment/update.html"
    form_class = SpecialAssignmentForm
    success_message = get_trans_txt("Special assignment updated successfully!")
    model = SpecialAssignment
    success_url = reverse_lazy("bookkeeper:special_assignment:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Update special assignment")
        # perm = self.request.user.get_user_permissions()
        # perm = self.request.user.get_group_permissions()
        # perm = self.request.user.user_permissions.all()
        # add permission
        # self.request.user.user_permissions.add(perm, perm2)
        # debugging_print(perm)
        return context

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        assigned_by = self.get_object().assigned_by
        kwargs = super().get_form_kwargs()
        kwargs.update({"assigned_by": assigned_by})
        return kwargs

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.object.is_seen = False
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        url = reverse_lazy(
            "bookkeeper:special_assignment:update", kwargs={"pk": self.get_object().pk}
        )
        return url


class SpecialAssignmentDeleteView(
    LoginRequiredMixin, BookkeeperAccessMixin, SuccessMessageMixin, DeleteView
):
    login_url = reverse_lazy("users:auth:login")
    model = SpecialAssignment
    template_name = "bookkeeper/special_assignment/delete.html"
    success_message: str = get_trans_txt("Special assignment deleted successfully!")
    success_url = reverse_lazy("bookkeeper:special_assignment:requested")
