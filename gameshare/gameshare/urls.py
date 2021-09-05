"""gameshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from games.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('register/', profile_register, name='register'),
    path('login/', profile_login, name='login'),
    path('', ItemsListView.as_view(), name='items_list'),
    path('games/', include('games.urls')),
    path('create/', GameCreateView.as_view(), name='create_game'),
    path('command/<int:id_>/<str:cmd>', ItemsControlerView.as_view(), name='item_control'),
]

if bool(settings.DEBUG):
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
