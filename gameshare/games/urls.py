from django.urls import path
from .views import GamesListView
from . import views


urlpatterns = [
    path('', GamesListView.as_view(), name='gameslist'),
]
