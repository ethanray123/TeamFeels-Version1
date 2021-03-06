from django.contrib import admin
from .models import Stream, Streamer, Lobby,\
    Subscription, Notification, Report, Comment


class StreamerLobby(admin.ModelAdmin):
    list_display = ('lobbies', 'title', 'streamers')
    list_filter = ['lobbies']


admin.site.register(Streamer)
admin.site.register(Lobby)
admin.site.register(Stream, StreamerLobby)
admin.site.register(Subscription)
admin.site.register(Notification)
admin.site.register(Report)
admin.site.register(Comment)
