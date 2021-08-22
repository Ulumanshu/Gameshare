from django.shortcuts import render
from django.http import HttpResponse
from .models import GamesItem
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
# Create your views here.


class GamesListView(ListView):
    model = GamesItem
    template_name = "gameslistitems.html"
