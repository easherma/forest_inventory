from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forest_inventory.forests.models import Forest, ForestTypeFilter

class ForestListView(ListView):
    context_object_name = 'forests'
    model = Forest
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = ForestTypeFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = ForestTypeFilter(self.request.GET, queryset)
        context["filter"] = filter
        return context


class ForestDetailView(DetailView):
    model = Forest
