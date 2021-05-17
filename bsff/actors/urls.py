from bsff.actors.models import Actor
from django.urls import path
from . import views

app_name = "actors"
urlpatterns = [
    path(
        route='',
        view = views.ActorListView.as_view(),
        name = 'list'
    )
]