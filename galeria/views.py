from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from galeria.models import Artwork, Artist  
from django.http import HttpResponse


# List Views
class ArtistListView(ListView):
     model = Artist

class ArtworkListView(ListView):
     model = Artwork

# Detail Views
class ArtistDetailView(DetailView):
     model = Artist

class ArtworkDetailView(DetailView):
     model = Artwork

# Create Views
class ArtistCreateView(CreateView):
     model = Artist
     fields = '_all_'


class ArtworkCreateView(CreateView):
     model = Artwork
     fields = '_all_'

# Update Views
class ArtistUpdateView(UpdateView):
     model = Artist
     fields = '_all_'

class ArtworkUpdateView(UpdateView):
     model = Artwork
     fields = '_all_'

# Delete Views
class ArtistDeleteView(DeleteView):
     model = Artist
     success_url = reverse_lazy('artist-list')

class ArtworkDeleteView(DeleteView):
     model = Artwork
     success_url = reverse_lazy('artwork-list')