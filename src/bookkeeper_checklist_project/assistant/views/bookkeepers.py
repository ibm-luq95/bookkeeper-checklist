from django.views.generic.base import TemplateView


class BookkeepersListView(TemplateView):
    template_name = "assistant/bookkeepers/list.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "Bookkeepers"
        return context
