from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormView

from core.utils.utils import get_trans_txt
from users.forms import CustomUserCreationForm, UpdateUserForm
from .mixins import ManagerAccessMixin


class UserCreateView(
    LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, CreateView
):
    # model = get_user_model()
    login_url = reverse_lazy("users:auth:login")
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

        context["title"] = get_trans_txt("Create User")
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
    login_url = reverse_lazy("users:auth:login")
    template_name: str = "manager/users/details.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Detail User"
        return context


class UserUpdateView(LoginRequiredMixin, ManagerAccessMixin, SuccessMessageMixin, FormView):
    login_url = reverse_lazy("users:auth:login")
    template_name = "manager/users/update.html"
    http_method_names = ["post", "get"]
    form_class = UpdateUserForm
    user_object = None

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        # this will handle if there is no ?user value in the url
        user_pk = self.request.GET.get("user")
        if not user_pk:
            return redirect(reverse_lazy("manager:manager:list"))
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = get_trans_txt("Update User")
        return context

    # def get_object(self):
    #     user_pk = self.request.GET.get("user")
    #     user = get_user_model().objects.get(pk=user_pk)
    #     return user

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        user_pk = self.request.GET.get("user")
        self.user_object = get_user_model().objects.get(pk=user_pk)
        kwargs.update({"instance": self.user_object})
        return kwargs

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        # self.object = form.save()
        password = form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")
        if password != "":
            if confirm_password == "":
                form.add_error("confirm_password", "Password confirmation required!")
                messages.error(self.request, "Password confirmation required!")
                return self.form_invalid(form)
            elif confirm_password != password:
                form.add_error("confirm_password", "Password confirmation not match!")
                messages.error(self.request, "Password confirmation not match!")
                return self.form_invalid(form)
            else:
                self.user_object.set_password(password)
                self.user_object.save()

        form.save()
        messages.success(self.request, "User updated successfully!")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self) -> str:
        view_name = self.request.resolver_match.view_name
        pk = self.request.GET.get("user")
        url = reverse_lazy(view_name) + f"?user={pk}"
        return url
