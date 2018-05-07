from django.views.generic import ListView, DetailView
from .models import Lobby, Streamer_lobby


class HomeView(ListView):
    model = Lobby
    template_name = "home.html"
    context_object_name = "lobbies"


class LobbyView(DetailView):
    model = Lobby
    template_name = "stream/lobby.html"
    context_object_name = "lobby"
