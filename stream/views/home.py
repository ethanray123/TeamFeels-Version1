from django.views.generic import ListView
from stream.models import Lobby, Streamer


class HomeView(ListView):
    model = Lobby
    template_name = "home.html"
    context_object_name = "lobbies"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            streamer = Streamer.objects.get(user=self.request.user)
            context['notifications'] = streamer.get_notifications()
        return context
