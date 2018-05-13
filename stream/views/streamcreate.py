from stream.models import Stream  # , Lobby
from django.views.generic.edit import CreateView
# from stream.forms import StreamForm
# from django.urls import reverse_lazy
# from django.shortcuts import get_object_or_404, render


class StreamCreateView(CreateView):
    model = Stream
    fields = ['title', 'thumbnail', 'lobbies']
    template_name = "stream/streamcreate_form.html"