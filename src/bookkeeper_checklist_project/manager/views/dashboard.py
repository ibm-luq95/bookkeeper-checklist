from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

from .mixins import ManagerAccessMixin


# from django.contrib.auth.models import Permission


class DashboardHomeView(LoginRequiredMixin, ManagerAccessMixin, TemplateView):
    template_name: str = "manager/dashboard/home.html"
    login_url = reverse_lazy("users:login")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Management"
        # Individual permissions
        # all_permissions = Permission.objects.filter(user=self.request.user)
        # cpprint(sorted(self.request.user.get_all_permissions()))
        # cpprint(self.request.user.has_perm("manager.manager_user"))
        # Permissions that the user has via a group
        # all_permissions = Permission.objects.filter(group__user=self.request.user)
        # cpprint(all_permissions)
        # cpprint(all_permissions.first().name)
        # cpprint(self.request.user.groups.all())
        return context
