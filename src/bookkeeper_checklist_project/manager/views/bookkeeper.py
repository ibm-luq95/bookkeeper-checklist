from bookkeeper.models import Bookkeeper
from django.views.generic import ListView, DetailView


class BookkeepersListView(ListView):
    template_name: str = "manager/bookkeeper/list.html"
    model = Bookkeeper
    paginate_by: int = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = "All bookkeepers"
        return context


class BookkeepersDetailsView(DetailView):
    template_name = "manager/bookkeeper/details.html"
    model = Bookkeeper

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "DetailView"
        return context
