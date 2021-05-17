from vanilla import CreateView, UpdateView, ListView, UpdateView
from vanilla.model_views import DetailView
from .models import Actor

class ActorListView(ListView):
    model = Actor
    

class ActorDetailView(DetailView):
    model = Actor
    lookup_field = 'slug'