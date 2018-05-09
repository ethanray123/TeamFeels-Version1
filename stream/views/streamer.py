from django.views.generic import DetailView
from stream.models import Streamer


class StreamerView(DetailView):
    model = Streamer
    template_name = "stream/streamerDetails.html"
    context_object_name = "streamer"
