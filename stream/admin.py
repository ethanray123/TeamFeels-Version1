from django.contrib import admin
from .models import Stream, Streamer, Lobby,\
    Subscription, Notification, Report


class StreamerLobby(admin.ModelAdmin):
    list_display = ('lobbies', 'streamers')
    list_filter = ['lobbies']


# class StreamerStream(admin.ModelAdmin):
#     list_display = ('title', 'streamer')
#     list_filter = ['title']


# admin.site.register(Stream, StreamerStream)
admin.site.register(Streamer)
admin.site.register(Lobby)
admin.site.register(Stream, StreamerLobby)
admin.site.register(Subscription)
admin.site.register(Notification)
admin.site.register(Report)
