from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import DeleteView, DetailView, ListView, CreateView, UpdateView

from bookkeeper.helpers import BookkeeperHelper
from bookkeeper.models import Bookkeeper
from bookkeeper.forms import BookkeeperForm, BookkeeperUpdateForm
from client.forms import ClientForm
from core.utils import get_trans_txt
from jobs.forms import JobForm
from task.forms import TaskForm
from .mixins import ManagerAccessMixin


class BookkeepersListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name: str = "manager/bookkeeper/list.html"
    model = Bookkeeper
    queryset = (
        Bookkeeper.objects.select_related()
        .filter(~Q(status="archive"))
        .order_by("-created_at")
    )

    # paginate_by: int = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("All bookkeepers")
        return context


class BookkeepersArchiveView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name: str = "manager/bookkeeper/archive_list.html"
    model = Bookkeeper
    queryset = (
        Bookkeeper.objects.select_related()
        .filter(Q(status="archive"))
        .order_by("-created_at")
    )

    # paginate_by: int = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("All bookkeepers")
        return context


class BookkeeperCreateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, CreateView
):
    login_url = reverse_lazy("users:login")
    template_name: str = "manager/bookkeeper/create.html"
    model = Bookkeeper
    success_url = get_trans_txt("Bookkeeper created successfully")
    form_class = BookkeeperForm
    success_url = reverse_lazy("manager:bookkeeper:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Create bookkeepers")
        return context


class BookkeeperUpdateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, UpdateView
):
    login_url = reverse_lazy("users:login")
    template_name: str = "manager/bookkeeper/update.html"
    model = Bookkeeper
    success_url = get_trans_txt("Bookkeeper updated successfully")
    form_class = BookkeeperUpdateForm
    success_url = reverse_lazy("manager:bookkeeper:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Update bookkeepers")
        return context

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs


class BookkeepersDetailsView(LoginRequiredMixin, ManagerAccessMixin, DetailView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/bookkeeper/details.html"
    model = Bookkeeper

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bookkeeper_fullname = self.get_object().user.fullname
        context["title"] = f"{bookkeeper_fullname}"
        context["jobs_form"] = JobForm(bookkeeper=self.get_object())
        context["client_form"] = ClientForm()
        context["task_form"] = TaskForm()
        # context["client_account_form"] = ClientAccountForm()
        context["bookkeeper_helper"] = BookkeeperHelper(bookkeeper=self.get_object())
        # print(context["jobs_form"].data)
        return context


class BookkeeperDeleteView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, DeleteView
):
    login_url = reverse_lazy("users:login")
    model = Bookkeeper
    template_name = "manager/bookkeeper/delete.html"
    success_message: str = get_trans_txt("Bookkeeper deleted successfully!")
    success_url = reverse_lazy("manager:bookkeeper:list")
