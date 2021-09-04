from django.urls import path
from .views import GamesListView, ItemsListView
from . import views

urlpatterns = [
    path('', GamesListView.as_view(), name='game_list'),
]
