from django.urls import path
from .views import GamesListView, GamesView
from . import views

urlpatterns = [
    path('list/', GamesListView.as_view(), name='gameslist'),
    path('list2/', GamesView),
]
