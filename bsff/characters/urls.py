from bsff.actors.models import Actor
from django.urls import path
from . import views

app_name = "characters"
urlpatterns = [
    path(
        route='',
        view = views.ActorListView.as_view(),
        name = 'list'
    ),
    path(
        route='add/',
        view = views.ActorCreateView.as_view(),
        name = 'add'
    ),
    path(
        route='<slug:slug>/update/',
        view = views.ActorUpdateView.as_view(),
        name = 'update'
    ),
    path(
        route='<slug:slug>/',
        view = views.ActorDetailView.as_view(),
        name = 'detail'
    ),
    
]