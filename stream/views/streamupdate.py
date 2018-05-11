from stream.models import Stream  # , Lobby
from django.views.generic.edit import UpdateView
from stream.forms import StreamForm
from django.urls import reverse_lazy
# from django.shortcuts import get_object_or_404, render


class StreamFormView(UpdateView):
    model = Stream
    form_class = StreamForm
    template_name = "stream/streamedit_form.html"

    def get_success_url(self):
        # lobbyid = self.request.GET.get('lobby_id')
        # lobby = get_object_or_404(Lobby, pk=lobbyid)
        # print(lobbyid)
        # return render(
        #     self.request, 'stream/lobby.html',
        #     {
        #         'lobby': lobby,
        #     })
        return reverse_lazy('stream:home')
