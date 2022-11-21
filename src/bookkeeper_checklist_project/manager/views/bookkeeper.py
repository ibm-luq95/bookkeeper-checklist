from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from bookkeeper.helpers import BookkeeperHelper
from bookkeeper.models import Bookkeeper
from client.forms import ClientForm
from jobs.forms import JobForm
from task.forms import TaskForm
from .mixins import ManagerAccessMixin


class BookkeepersListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name: str = "manager/bookkeeper/list.html"
    model = Bookkeeper
    # paginate_by: int = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "All bookkeepers"
        return context


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
    success_message: str = "Bookkeeper deleted successfully!"
    success_url = reverse_lazy("manager:bookkeeper:list")
