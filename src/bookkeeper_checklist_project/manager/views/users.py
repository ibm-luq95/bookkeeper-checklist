from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from assistant.models import Assistant
from bookkeeper.models import Bookkeeper
from core.utils import debugging_print
from users.forms import CustomUserCreationForm
from .mixins import ManagerAccessMixin


class UserCreateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, CreateView
):
    # model = get_user_model()
    login_url = reverse_lazy("users:login")
    template_name = "manager/users/create.html"
    form_class = CustomUserCreationForm
    http_method_names = ["post", "get"]
    success_message = "User created successfully!"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        user_object = self.object
        user_type = form.cleaned_data.get("user_type")
        if user_type == "bookkeeper":
            bookkeeper_object = Bookkeeper.objects.create(user=user_object)
        elif user_type == "assistant":
            assistant_object = Assistant.objects.create(user=user_object)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["title"] = "Create User"
        return context

    # def get_form(self, form_class=None):
    #     """Return an instance of the form to be used in this view."""
    #     if form_class is None:
    #         user_type = self.request.GET.get("user_type", None)
    #         form_class = self.get_form_class()
    #         if user_type:
    #             form_class.fields["user_type"]
    #     return form_class(**self.get_form_kwargs())
    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        user_type = self.request.GET.get("user_type", None)
        if user_type:
            initial["user_type"] = user_type

        return initial


class UserDetailsView(LoginRequiredMixin, ManagerAccessMixin, DetailView):
    model = get_user_model()
    login_url = reverse_lazy("users:login")
    template_name: str = "manager/users/details.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail User"
        return context
