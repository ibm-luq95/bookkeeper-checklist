from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ImproperlyConfigured
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

    # def form_valid(self, form):
    #     """If the form is valid, save the associated model."""
    #     self.object = form.save()
    #     user_object = self.object
    #     user_type = form.cleaned_data.get("user_type")
    #     if user_type == "bookkeeper":
    #         bookkeeper_object = Bookkeeper.objects.create(user=user_object)
    #     elif user_type == "assistant":
    #         assistant_object = Assistant.objects.create(user=user_object)
    #     return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["title"] = "Create User"
        return context

    # def get_success_url(self):
    #     """Return the URL to redirect to after processing a valid form."""
    #     if self.success_url:
    #         # debugging_print("IN IF")
    #         url = self.success_url.format(**self.object.__dict__)
    #     else:
    #         try:
    #             url = self.object.get_absolute_url()
    #             new_user = self.object
    #             if new_user.user_type == "bookkeeper":
    #                 url = reverse_lazy(
    #                     "manager:bookkeeper:details", kwargs={"slug": self.object.slug}
    #                 )
    #         except AttributeError:
    #             raise ImproperlyConfigured(
    #                 "No URL to redirect to.  Either provide a url or define"
    #                 " a get_absolute_url method on the Model."
    #             )
    #     return url

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        user_type = self.request.GET.get("user_type", None)
        if user_type:
            if user_type in ["bookkeeper", "assistant"]:
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
