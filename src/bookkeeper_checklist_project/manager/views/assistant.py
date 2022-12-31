from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from assistant.models import Assistant
from assistant.forms import AssistantForm
from core.utils import get_trans_txt, debugging_print
from .mixins import ManagerAccessMixin


class AssistantListView(LoginRequiredMixin, ManagerAccessMixin, ListView):
    login_url = reverse_lazy("users:login")
    template_name: str = "manager/assistant/list.html"
    model = Assistant

    # paginate_by: int = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("All assistants")
        return context


class AssistantDetailsView(LoginRequiredMixin, ManagerAccessMixin, DetailView):
    login_url = reverse_lazy("users:login")
    template_name = "manager/assistant/details.html"
    model = Assistant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assistant_fullname = self.get_object().user.fullname
        context["title"] = f"{assistant_fullname}"
        # print(context["jobs_form"].data)
        return context


class AssistantUpdateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, UpdateView
):
    login_url = reverse_lazy("users:login")
    template_name = "manager/assistant/update.html"
    model = Assistant
    http_method_names = ["post", "get"]
    form_class = AssistantForm
    success_message = get_trans_txt("Assistant updated successfully")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assistant_fullname = self.get_object().user.fullname
        context["title"] = f"Update - {assistant_fullname}"
        return context

    def get_success_url(self):
        url = reverse_lazy("manager:assistant:update", kwargs={"pk": self.get_object().pk})
        return url


class AssistantDeleteView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, DeleteView
):
    login_url = reverse_lazy("users:login")
    model = Assistant
    template_name = "manager/assistant/delete.html"
    success_message: str = get_trans_txt("Assistant deleted successfully!")
    success_url = reverse_lazy("manager:assistant:list")
