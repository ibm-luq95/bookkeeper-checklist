import random
from datetime import datetime

import requests
from core.models import Quote
from core.utils import get_formatted_logger
from django.views.generic.base import TemplateView

# TODO: remove the custom logger before push (only for development)
# ###### [Custom Logger] #########
logger = get_formatted_logger(__name__)


# ###### [Custom Logger] #########


class DashboardView(TemplateView):
    template_name = "bookkeeper/dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        try:
            context = super().get_context_data(**kwargs)
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

            context["title"] = "Bookkeeper - Dashboard"
            context.setdefault("quote_text", quote_text)
            context["bookkeeper_name"] = self.request.user.fullname
            return context
        except requests.exceptions.ConnectionError:
            return None
        except Exception as ex:
            logger.error(ex)
            raise
