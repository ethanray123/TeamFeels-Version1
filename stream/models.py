from django.db import models
from django.contrib.auth.models import User


class Streamer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='streamer_info'
    )

    def __str__(self):
        return self.user.username

    @property
    def lobbies(self):
        return self.streamer_in_lobby.filter(streamers=self)

    def subcribes(self, publisher):
        if not self == publisher:
            Subscription.objects.create(subscriber=self, publisher=publisher)

    def unsubscibes(self, publisher):
        Subscription.objects.filter(
            subscriber=self, publisher=publisher).delete()

    def create_notification(self, description):
        Notification.objects.create(publisher=self, description=description)

    def get_notifications(self):
        publishers = Subscription.objects.values(
            "publisher").filter(subscriber=self)
        notification = Notification.objects.filter(
            publisher__in=publishers).order_by('-published')[:5]
        return notification

    def get_all_notifications(self):
        publishers = Subscription.objects.values(
            "publisher").filter(subscriber=self)
        notification = Notification.objects.filter(
            publisher__in=publishers).order_by('-published')
        return notification
        # publishers = Subscription.objects.filter(
        #     subscriber=self)
        # return Notification.objects.filter(
        #     publisher=publishers.objects.values("publisher"))


# Not sure if this is right but ImageField requires pip install Pillow to use
# If this is a wrong approach then just change it temporarily to CharField
class Stream(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(
        upload_to='stream/static/images', blank=True, null=True)
    streamer = models.ForeignKey(
        Streamer,
        on_delete=models.PROTECT,
        related_name="stream_owner"
    )

    def __str__(self):
        return self.title


# Not sure if this is right but ImageField requires pip install Pillow to use
# If this is a wrong approach then just change it temporarily to CharField
class Lobby(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='lobby_owner'
    )

    lobbyname = models.CharField(max_length=50)
    # Set a default image
    logo = models.ImageField(
        upload_to='stream/static/images', blank=True, null=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.lobbyname

    @property
    # Get Streamers in this Lobby
    def streamers(self):
        return self.lobby_of_streamer.streamer.filter(lobby=self)

    # Get Streams of Streamers in this Lobby
    def streams(self):
        return self.lobby_of_streamer.stream_owner.filter(lobby=self)


# "Bridge" between streamers and lobby to prevent use of ManyToMany Field
class Streamer_lobby(models.Model):
    streamer = models.ForeignKey(
        Streamer,
        on_delete=models.PROTECT,
        related_name='streamer_in_lobby',
        null=True
    )
    lobby = models.ForeignKey(
        Lobby,
        on_delete=models.CASCADE,
        related_name='lobby_of_streamer'
    )


class Subscription(models.Model):
    subscriber = models.ForeignKey(
        Streamer,
        on_delete=models.CASCADE, related_name='subscribers')
    publisher = models.ForeignKey(
        Streamer,
        on_delete=models.CASCADE, related_name='publishers')

    def __str__(self):
        return ("{} subcribes to {}").format(self.subscriber, self.publisher)


class Notification(models.Model):
    publisher = models.ForeignKey(Streamer, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} : {} : {}".format(
            self.publisher,
            self.description,
            self.published.strftime("%b %d, %Y at %I:%M:%S %p"))

    def display(self):
        return "{} : {} : {}".format(
            self.publisher,
            self.description,
            self.published.strftime("%b %d, %Y at %I:%M:%S %p"))
