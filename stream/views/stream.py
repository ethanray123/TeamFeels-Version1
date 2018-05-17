from stream.models import Stream, Streamer  # , Lobby
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from stream.forms import StreamForm
# from stream.forms import StreamForm


class StreamCreateView(generic.CreateView):
    model = Stream
    fields = ['title', 'thumbnail', 'lobbies']
    template_name = "stream/streamcreate_form.html"
    success_url = reverse_lazy('stream:home')

    def form_valid(self, form):
        # store data locally
        stream = form.save(commit=False)
        current_streamer = Streamer.objects.get(user=self.request.user)
        stream.streamers = current_streamer
        # save in database
        stream.save()
        return HttpResponseRedirect(reverse_lazy('stream:home'))


class StreamUpdateView(generic.UpdateView):
    model = Stream
    form_class = StreamForm
    template_name = "stream/streamedit_form.html"

    def get_success_url(self):
        return reverse_lazy('stream:home')


class StreamDeleteView(generic.DeleteView):
    model = Stream
    success_url = reverse_lazy('stream:home')
