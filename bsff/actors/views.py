from vanilla import CreateView, UpdateView, ListView, UpdateView
from .models import Actor

class ActorListView(ListView):
    model = Actor
