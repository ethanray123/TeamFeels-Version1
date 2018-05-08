from django.views.generic import DetailView
from stream.models import Lobby


class LobbyView(DetailView):
    model = Lobby
    template_name = "stream/lobby.html"
    context_object_name = "lobby"
