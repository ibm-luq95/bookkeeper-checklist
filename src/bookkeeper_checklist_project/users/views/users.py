from typing import List, Optional
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib import messages

from users.forms import CustomUserLoginForm
from prettyprinter import cpprint
from termcolor import cprint


class LoginView(SuccessMessageMixin, FormView):
    http_method_names = ["post", "get"]
    success_url = reverse_lazy("users:login")
    template_name = "users/login.html"
    form_class = CustomUserLoginForm
    success_message: str = "Login successfully"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = "Login"
        return context
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # print(form)
        # cprint(reverse_lazy("users:assistant-urls"), "green")
        if form.cleaned_data.get("user_type") == "assistant":
            return redirect("assistant:assistant-dashboard")
        elif form.cleaned_data.get("user_type") == "bookkeeper":
            return redirect("bookkeeper:bookkeeper-dashboard")
        cpprint(form.cleaned_data)
        # messages.success(self.request, "Login Success")
        return super().form_valid(form)
