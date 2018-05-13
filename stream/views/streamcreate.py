from stream.models import Stream, Lobby
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from stream.forms import StreamForm
from django.shortcuts import render, reverse
# from django.urls import reverse_lazy
# from django.shortcuts import get_object_or_404, render


class StreamCreateView(CreateView):
    model = Stream
    form_class = StreamForm
    template_name = "stream/streamcreate_form.html"

    # def get(self, request, lobby_id):
    #     form = self.form_class(StreamForm)
    #     return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = StreamForm(request.POST, user=request.user)

        if form.is_valid():
            stream = form.save(commit=False)
            # lobbyid = lobby_id # self.kwargs.get('lobby_id')
            # lobby = get_object_or_404(Lobby, pk=lobbyid)
            lobby = form.cleaned_data.get('lobbies')
            stream.lobbies = lobby
            stream.save()
            return HttpResponseRedirect(
                reverse('stream:lobby-detail', args=[lobbyid]))
        return render(request, self.template_name, {'form': form})