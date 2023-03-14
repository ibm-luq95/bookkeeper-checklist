import random
from datetime import datetime

import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import SingleObjectMixin

from bookkeeper.helpers import BookkeeperHelper
from core.models import Quote
from core.utils import get_formatted_logger
from .mixins import BookkeeperAccessMixin
from ..models import BookkeeperProxy

# TODO: remove the custom logger before push (only for development)
# ###### [Custom Logger] #########
logger = get_formatted_logger()


# ###### [Custom Logger] #########


class DashboardView(LoginRequiredMixin, BookkeeperAccessMixin, TemplateView):
    template_name = "bookkeeper/dashboard/dashboard.html"
    login_url = reverse_lazy("users:auth:login")
    model = BookkeeperProxy

    # def dispatch(self, *args, **kwargs):
    #     self.object = self.get_object()
    #     return super().dispatch(*args, **kwargs)

    # def get_queryset(self):
    #     print(type(self.request.user.bookkeeper))
    #     return self.request.user.bookkeeper

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        try:
            context = super().get_context_data(**kwargs)
            groups = self.request.user.groups.all()
            # debugging_print(groups)
            today = datetime.now()
            quote_text = ""
            quote_keywords = (
                "Inspiration",
                "Love",
                "Pain",
                "Past",
                "Success",
                "Work",
                "Today",
                "Happiness",
                "Life",
                "Dreams",
            )
            get_quote_object = Quote.objects.filter(
                created_at__year=today.year,
                created_at__month=today.month,
                created_at__day=today.day,
                user=self.request.user,
            )

            if get_quote_object:
                get_quote_object = get_quote_object.first()
                quote_text = get_quote_object.quote_text
            else:
                try:

                    quote_choice = random.choice(quote_keywords)
                    quote_url = f"https://zenquotes.io/api/random/{quote_choice}"
                    quote_req = requests.get(quote_url)
                    quote_item = quote_req.json()[0]
                    quote_object = Quote()
                    quote_object.quote_choice = quote_choice
                    quote_object.author = quote_item.get("a")
                    quote_object.quote_text = quote_item.get("q")
                    quote_object.full_quote_object = quote_item
                    quote_object.user = self.request.user  # TODO: Enable it after fix auth
                    quote_object.save()
                    quote_text = quote_object.quote_text
                except requests.exceptions.ConnectionError:
                    pass

            context["title"] = "Bookkeeper - Dashboard"
            context.setdefault("quote_text", quote_text)
            context["bookkeeper_name"] = self.request.user.fullname
            # bookkeeper = self.request.user.bookkeeper
            bookkeeper = BookkeeperProxy.objects.get(pk=self.request.user.bookkeeper.pk)
            # debugging_print("#################################")
            # debugging_print(self.request.user.bookkeeper.special_assignments.select_related())
            # debugging_print(self.request.user.bookkeeper)
            # cpprint(sorted(self.request.user.get_all_permissions()))
            # cpprint(self.request.user.has_perm("bookkeeper.bookkeeper_user"))
            # debugging_print("#################################")
            context.setdefault("bookkeeper", bookkeeper)
            # bookkeeper_helper = BookkeeperHelper(bookkeeper)
            # context.setdefault("clients", bookkeeper_helper.get_clients())
            # context.setdefault(
            #     "total_past_due_total", bookkeeper_helper.get_past_due_tasks_total
            # )
            context.setdefault("last_tasks", bookkeeper.get_last_tasks())
            return context

        except Exception as ex:
            logger.error(ex)
            raise
