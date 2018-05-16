import json
from django.shortcuts import get_object_or_404
from stream.models import Subscription, Streamer
from django.views.generic import View
from django.http import HttpResponse, Http404


class SubscribeView(View):

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404
        subscriber = get_object_or_404(Streamer, user=request.user)
        subscribee = get_object_or_404(Streamer, pk=request.GET['streamer_id'])
        if(not subscribee.is_subscribed(subscriber) and
           subscriber.user.username != subscribee.user.username):
            Subscription.objects.create(
                subscriber=subscriber,
                publisher=subscribee)
            message = "you are now subscribed to " \
                + subscribee.user.username + "!"
        else:
            if(subscribee.is_subscribed(subscriber)):
                message = "you have already subscribed to " \
                    + subscribee.user.username
            else:
                message = "you cannot subscribe to yourself"
        data = {
            'message': message}
        return HttpResponse(json.dumps(data), content_type="application/json")
