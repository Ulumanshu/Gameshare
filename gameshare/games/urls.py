from django.urls import path
from .views import GamesListView, ItemsListView
from . import views

urlpatterns = [
    path('games/', GamesListView.as_view(), name='game_list'),
    path('items/', ItemsListView.as_view(), name='item_list'),
]
