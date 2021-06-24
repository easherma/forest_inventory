from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forests.models import Forest

class ForestListView(ListView):
    context_object_name = 'forests'
    model = Forest
    paginate_by = 6

class ForestDetailView(DetailView):
    model = Forest
