from stream.models import Stream, Streamer  # , Lobby
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# from stream.forms import StreamForm


class StreamCreateView(CreateView):
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
        # return self.form_valid(form)
        return HttpResponseRedirect(reverse_lazy('stream:home'))
    # def post(self, request):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     if form.is_valid():
    #         # store data locally
    #         stream = form.save(commit=False)
    #         current_streamer = Streamer.objects.get(user=self.request.user)
    #         stream.streamers = current_streamer
    #         # save in database
    #         stream.save()
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
