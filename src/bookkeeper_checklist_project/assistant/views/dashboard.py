from django.views.generic.base import TemplateView
import faker

class DashboardView(TemplateView):
    template_name = "assistant/dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Assistant - Dashboard"
        fake = faker.Faker()
        context["assistant_fake_name"] = fake.name()
        return context
