from django.contrib import admin
from .models import Stream, Streamer, Lobby, Streamer_lobby

class StreamerLobby(admin.ModelAdmin):
    list_display = ('lobbies', 'streamers')
    list_filter = ['lobbies']


admin.site.register(Stream)
admin.site.register(Streamer)
admin.site.register(Lobby)
admin.site.register(Streamer_lobby, StreamerLobby)
