from vanilla.model_views import DetailView, UpdateView, CreateView, ListView
from .models import Actor
from django.contrib.auth.mixins import LoginRequiredMixin

class ActorListView(ListView):
    model = Actor
    

class ActorDetailView(DetailView):
    model = Actor
    lookup_field = 'slug'

class ActorCreateView(LoginRequiredMixin,CreateView):
    model = Actor
    fields = [
        'full_name', 'short_name', 'bio',
    ]

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class ActorUpdateView(LoginRequiredMixin,UpdateView):
    model = Actor
    lookup_field = 'slug'
    fields = [
        'full_name', 'short_name', 'bio',
    ]
    
    action = "update"