from django.views.generic.base import TemplateView
import faker
from core.models import Quote
import requests
from datetime import datetime
import random
from prettyprinter import cpprint


class DashboardView(TemplateView):
    template_name = "bookkeeper/dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
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
            # user=self.request.user  # TODO: Enable it after fix auth
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
            # quote_object.user = self.request.user  # TODO: Enable it after fix auth
            quote_object.save()
            quote_text = quote_object.quote_text

        context["title"] = "Bookkeeper - Dashboard"
        context.setdefault("quote_text", quote_text)
        fake = faker.Faker()
        context["bookkeeper_fake_name"] = fake.name()
        return context
