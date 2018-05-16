import json
from django.views.generic import DetailView, View, DeleteView, CreateView, \
    UpdateView
from stream.models import Lobby, Comment, Streamer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from stream.forms import LobbyForm
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class LobbyView(DetailView):
    model = Lobby
    template_name = "stream/lobby.html"
    context_object_name = "lobby"

    def get_context_data(self, **kwargs):
        context = super(LobbyView, self).get_context_data(**kwargs)
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
        data = {
            'comments': list(comments)}
        return HttpResponse(
            json.dumps(data), content_type="application/json")


class CreateLobbyView(CreateView):
    model = Lobby
    form_class = LobbyForm
    template_name = "stream/createlobby_form.html"

    def form_valid(self, form):
        lobby = form.save(commit=False)
        lobby.owner = self.request.user
        lobby.save()
        return HttpResponseRedirect(
            reverse('stream:lobby-detail', args=[lobby.pk]))


class UpdateLobbyView(UpdateView):
    model = Lobby
    form_class = LobbyForm
    template_name = "stream/updatelobby_form.html"

    def get_success_url(self):
        return reverse('stream:lobby-detail', args=[self.object.pk])


class DeleteLobbyView(DeleteView):
    model = Lobby
    success_url = reverse_lazy('stream:home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
