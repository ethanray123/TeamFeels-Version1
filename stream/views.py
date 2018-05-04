from django.views.generic import ListView
from .models import Lobby


class HomeView(ListView):
    model = Lobby
    template_name = "home.html"
    context_object_name = "lobbies"

class LobbyView(ListView):
	model = Lobby
	template_name = "stream/lobby.html"
	context_object_name = "lobbies"