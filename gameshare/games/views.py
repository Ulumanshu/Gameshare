from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from .models import Games, Items
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
# Create your views here.


class GamesListView(ListView):
    model = Games
    all_games = Games.objects.all()
    games_count = Games.objects.count()
    context = {
        'all_items': all_games,
        'games_count': games_count,
    }
    template_name = "gameslistitems.html"


class ItemsListView(ListView):
    model = Items
    all_items = Items.objects.all()
    items_count = Items.objects.count()
    context = {
        'all_items': all_items,
        'items_count': items_count,
    }
    template_name = "itemslist.html"
