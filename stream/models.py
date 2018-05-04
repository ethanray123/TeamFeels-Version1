from django.db import models
from django.contrib.auth.models import User


class Streamer(models.Model):
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='name'
    )

    def __str__(self):
        return self.username.get_full_name()


# Not sure if this is right but ImageField requires pip install Pillow to use
# If this is a wrong approach then just change it temporarily to CharField
class Stream(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='stream/static/images', blank=True)
    streamer = models.ForeignKey(Streamer, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


# Not sure if this is right but ImageField requires pip install Pillow to use
# If this is a wrong approach then just change it temporarily to CharField
class Lobby(models.Model):
    lobbyname = models.CharField(max_length=50)
    # Set a default image
    logo = models.ImageField(upload_to='stream/static/images', blank=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.lobbyname


# "Bridge" between streamers and lobby to prevent use of ManyToMany Field
class Streamer_lobby(models.Model):
    streamers = models.ForeignKey(
        Streamer,
        on_delete=models.PROTECT,
        related_name='name',
        null=True
    )
    lobbies = models.ForeignKey(
        Lobby,
        on_delete=models.CASCADE,
        related_name='streamers'
    )
