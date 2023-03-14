from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
# from django.contrib.sites.models import Site

from core.cache import CacheViewMixin
from core.utils import get_trans_txt
from .mixins import ManagerAccessMixin
from task.models import Task
from client.models import Client
from special_assignment.models import SpecialAssignment
from jobs.models import Job
from bookkeeper.models import Bookkeeper


# from django.contrib.auth.models import Permission

from core.utils import get_formatted_logger

logger = get_formatted_logger()


class DashboardHomeView(LoginRequiredMixin, ManagerAccessMixin, CacheViewMixin, TemplateView):
    template_name: str = "manager/dashboard/home.html"
    login_url = reverse_lazy("users:auth:login")
    http_method_names = ["get"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Management"))
        context.setdefault("web_app_settings_cache", self.cmx_get_item("web_app_settings"))
        all_tasks = Task.objects.select_related().filter()
        all_jobs = Job.objects.select_related().filter()
        all_special_assignments = SpecialAssignment.objects.select_related().filter()
        all_clients = Client.objects.select_related().filter()
        all_bookkeepers = Bookkeeper.objects.select_related().filter()[:5]
        # logger.info("WWWWWWWWWWWWWWWWW")
        # site = Site.objects.get_current()
        # print(site)
        # raise Exception("Stop")
        context.setdefault("all_tasks", all_tasks)
        context.setdefault("all_jobs", all_jobs)
        context.setdefault("all_clients", all_clients)
        context.setdefault("all_bookkeepers", all_bookkeepers)
        context.setdefault("all_special_assignments", all_special_assignments)
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
