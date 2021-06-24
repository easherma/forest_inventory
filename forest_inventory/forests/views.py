from django.shortcuts import render
from django.views.generic import ListView, DetailView
from forests.models import Forest

class ForestListView(ListView):
    model = Forest

class ForestDetailView(DetailView):
    model = Forest
