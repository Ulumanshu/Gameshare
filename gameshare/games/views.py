from .models import Games, Items
from .forms import GameForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .forms import ProfileRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from django.core.files.storage import Storage, default_storage



# Create your views here.


class GamesListView(ListView):
    model = Games
    all_games = Games.objects.all()
    #   games_count = GamesItems.objects.count()
    context = {
        'all_games': all_games,
        #    'games_count': games_count,
    }
    template_name = "gameslistitems.html"


class ItemsListView(ListView):
    model = Items
    template_name = "base.html"

    def get(self, request):
        all_items = Items.objects.all()
        items_count = Items.objects.count()
        # Render the HTML template passing data in the context.
        # if self.request.user.is_authenticated:
        #     posts = Items.objects.all().order_by('-published_date')
        # else:
        #     posts = Items.objects.filter(public=True).order_by('-published_date')
        context = {
            'all_items': all_items,
            'items_count': items_count,
        }
        return render(request, 'itemslist.html', context=context)


class GameCreateView(LoginRequiredMixin, CreateView):
    model = Games
    template_name = "creategame.html"
    fields = [
        'name',
        'photo',
        'author',
        'description',
        'pub_date',
        'label',
    ]
    # success_url = "/list/"

    def post(self, request):
        context = {}
        print(request.POST)
        if request.method == "POST":
            form = GameForm(data=request.POST, files=request.FILES)
            print('forma validi : ', form.is_valid())
            print('forma validi : ', form.errors)
            print(request.FILES)
            print("DEFAULT STORAGE: ", default_storage)

            if form.is_valid():
                print(form.cleaned_data['photo'])
                form.save()
                return render(request, 'gameslist.html', context=context)
            else:
                context.update(form=GameForm)
                return render(request, 'creategame.html', context=context)


    def get(self, request):
        context = {'form': GameForm}
        return render(request, 'creategame.html', context=context)


class GameUpdateView(PermissionRequiredMixin, UpdateView):
    model = GamesListView
    template_name = "updategame.html"
    fields = [
        'name',
        'author',
        'description ',
        'pub_date',
        'label',
    ]
    success_url = "/list/"


class GameDeleteView(PermissionRequiredMixin, DeleteView):
    model = GamesListView
    template_name = "deletegame.html"
    fields = [
        'name',
        'author',
        'description ',
        'pub_date',
        'label',
    ]
    success_url = "/list/"


def profile_register(request):
    form = ProfileRegisterForm()
    if request.method == 'POST':
        form = ProfileRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/login/')
    else:
        form = ProfileRegisterForm()
    return render(request, 'register.html', {'form': form})


def profile_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/list/')
            else:
                return HttpResponse('User not active')
        else:
            return HttpResponse('Error')
    return render(request, 'login.html', {})


def profile_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
