import json
from django.views.generic import ListView, View
from stream.models import Lobby, Streamer, Stream
from django.http import HttpResponse, Http404
from django.urls import reverse


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


class SearchView(View):

    def get(self, request, *args, **kwargs):
        # if(request.is_ajax()):
        if not request.is_ajax():
            raise Http404

        text = request.GET['search_text']
        streamers = Streamer.objects.filter(
            user__username__icontains=text).values('pk', 'user__username')[:5]
        streams = Stream.objects.filter(
            title__icontains=text).values('pk', 'title')[:5]
        lobbies = Lobby.objects.filter(
            lobbyname__icontains=text).values('pk', 'lobbyname')[:5]
        data = {
            'streamers': list(streamers),
            'streams': list(streams),
            'lobbies': list(lobbies),
            'streamer_url': reverse('stream:streamer-detail', args=[0]),
            'lobby_url': reverse('stream:lobby-detail', args=[0])}
        return HttpResponse(
            json.dumps(data), content_type="application/json")
