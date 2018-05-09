from django.shortcuts import get_object_or_404, render
from stream.models import Subscription, Streamer


def subscribe(request, streamer_id):
    subscriber = get_object_or_404(Streamer, user=request.user)
    subscribee = get_object_or_404(Streamer, pk=streamer_id)
    if(not subscribee.is_subscribed(subscriber) and
       subscriber.user.username != subscribee.user.username):
        Subscription.objects.create(
            subscriber=subscriber,
            publisher=subscribee)
        message = "you are now subscribed to " + subscribee.user.username + "!"
    else:
        if(subscribee.is_subscribed(subscriber)):
            message = "you have already subscribed to " \
                + subscribee.user.username
        else:
            message = "you cannot subscribe to yourself"
    return render(
        request, 'stream/subscribe.html',
        {
            'message': message,
        }
    )
