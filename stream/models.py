from django.db import models
from django.contrib.auth.models import User


class Streamer(models.Model):
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='name'
    )
    lobby = models.CharField(max_length=50)


# Not sure if this is right but ImageField requires pip install Pillow to use
# If this is a wrong approach then just change it temporarily to CharField
class Stream(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to=None)
    streamer = models.ForeignKey(Streamer, on_delete=models.PROTECT)


# Not sure if this is right but ImageField requires pip install Pillow to use
# If this is a wrong approach then just change it temporarily to CharField
class Lobby(models.Model):
    lobbyname = models.CharField(max_length=50)
    streamers = models.CharField(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=None)
    description = models.CharField(max_length=200)


# "Bridge" between streamers and lobby to prevent use of ManyToMany Field
class Streamer_lobby(models.Model):
    user = models.ForeignKey(
        Streamer,
        on_delete=models.PROTECT,
        related_name='name'
    )
    lobbies = models.ForeignKey(
        Lobby,
        on_delete=models.CASCADE,
        related_name='streamers'
    )
