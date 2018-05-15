from stream.models import Stream  # , Lobby
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# from stream.forms import StreamForm
# from django.shortcuts import get_object_or_404, render


class StreamCreateView(CreateView):
    model = Stream
    fields = ['title', 'thumbnail', 'lobbies']
    template_name = "stream/streamcreate_form.html"

    def get_success_url(self):
        return reverse_lazy('stream:home')

