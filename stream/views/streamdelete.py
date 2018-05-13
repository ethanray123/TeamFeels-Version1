from stream.models import Stream
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


class StreamDeleteView(DeleteView):
    model = Stream
    success_url = reverse_lazy('stream:home')