from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView

from users.forms import CustomUserCreationForm
from bookkeeper.models import Bookkeeper
from assistant.models import Assistant


class UserCreateView(SuccessMessageMixin, CreateView):
    # model = get_user_model()
    template_name = "manager/users/create.html"
    form_class = CustomUserCreationForm
    http_method_names = ["post", "get"]
    success_message: str = "New user created successfully"

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


class UserDetailsView(DetailView):
    model = get_user_model()
    template_name: str = "manager/users/details.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail User"
        return context
