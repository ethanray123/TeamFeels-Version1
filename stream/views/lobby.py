import json

from django.views.generic import DetailView, View
from stream.models import Lobby, Comment, Streamer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404


class LobbyView(DetailView):
    model = Lobby
    template_name = "stream/lobby.html"
    context_object_name = "lobby"

    def get_context_data(self, **kwargs):
        context = super(LobbyView, self).get_context_data(**kwargs)
        print(self.kwargs.get('pk'))
        lobby = get_object_or_404(Lobby, pk=self.kwargs.get('pk'))
        context['lobby'] = lobby
        context['comments'] = Comment.objects.filter(
            lobby=lobby).order_by('published')
        return context


class CommentView(View):

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404

        text = request.GET['comment_text']
        publisher = Streamer.objects.get(user=self.request.user)
        lobby = Lobby.objects.get(pk=request.GET['lobby_pk'])
        comments = Comment.objects.create(
            lobby=lobby,
            publisher=publisher,
            comment=text)
        data = {
            'comments': list(comments)}
        return HttpResponse(
            json.dumps(data), content_type="application/json")

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404
        lobby = Lobby.objects.get(pk=request.GET['lobby_pk'])
        if request.GET['valid']:
            text = request.GET['comment_text']
            publisher = Streamer.objects.get(user=self.request.user)
            comments = Comment.objects.create(
                lobby=lobby,
                publisher=publisher,
                comment=text)
        comments = Comment.objects.filter(lobby=lobby).values(
            'pk', 'publisher__user__username', 'comment')

        # text = request.GET['comment_text']
        # publisher = Streamer.objects.get(user=self.request.user)
        # lobby = Lobby.objects.get(pk=request.GET['lobby_pk'])
        # comment = Comment.objects.create(
        #     lobby=lobby,
        #     publisher=publisher,
        #     comment=text)
        data = {
            'comments': list(comments)}
        return HttpResponse(
            json.dumps(data), content_type="application/json")
