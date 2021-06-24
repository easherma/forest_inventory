from django.shortcuts import render
from django.views.generic import ListView
from forests.models import Forest

class ForestListView(ListView):
    model = Forest
