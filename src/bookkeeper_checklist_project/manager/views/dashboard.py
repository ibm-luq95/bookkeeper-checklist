from . import ManagerAccessMixin
from django.contrib.auth.models import Permission

from django.views.generic.base import TemplateView

from prettyprinter import cpprint


class DashboardHomeView(ManagerAccessMixin, TemplateView):

    template_name: str = "manager/dashboard/home.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Management"
        # Individual permissions
        # all_permissions = Permission.objects.filter(user=self.request.user)

        # Permissions that the user has via a group
        all_permissions = Permission.objects.filter(group__user=self.request.user)
        # cpprint(all_permissions)
        # cpprint(all_permissions.first().name)
        cpprint(self.request.user.groups.all())
        return context