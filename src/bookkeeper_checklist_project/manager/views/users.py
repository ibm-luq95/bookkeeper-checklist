from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView

from users.forms import CustomUserCreationForm


class UserCreateView(SuccessMessageMixin, CreateView):
    # model = get_user_model()
    template_name = "manager/users/create.html"
    form_class = CustomUserCreationForm
    http_method_names = ["post", "get"]
    success_message: str = "New user created successfully"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Create User"
        return context


class UserDetailsView(DetailView):
    model = get_user_model()
    template_name: str = "manager/users/details.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail User"
        return context
