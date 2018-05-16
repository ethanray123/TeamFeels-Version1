from django.urls import path
from .views import (
    HomeView, UserFormView, LobbyView,
    StreamerView, SubscribeView, ReportView, SearchView, StreamFormView,
    CreateLobbyView, CommentView, UpdateLobbyView, DeleteLobbyView,
    StreamCreateView, StreamDeleteView)


app_name = 'stream'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', UserFormView.as_view(), name='register'),
    path('streamedit/<int:pk>/<int:lobby_id>',
         StreamFormView.as_view(),
         name='edit_stream'),
    path('lobby/<int:pk>', LobbyView.as_view(),
         name='lobby-detail'),
    path('streamer/<int:pk>', StreamerView.as_view(),
         name='streamer-detail'),
    path('lobby/subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('search_result/', SearchView.as_view(), name='search_view'),
    path('lobby/comments/',
         CommentView.as_view(), name='comment_view'),
    path('lobby/report/', ReportView.as_view(), name='report'),
    path('lobby/create_lobby',
         CreateLobbyView.as_view(), name='create_lobby'),
    path('lobby/<int:pk>/update_lobby',
         UpdateLobbyView.as_view(), name='update_lobby'),
    path('lobby/<int:pk>/delete_lobby',
         DeleteLobbyView.as_view(), name='delete_lobby'),
    path('add/', StreamCreateView.as_view(), name='create_stream'),
    path('remove/<int:pk>', StreamDeleteView.as_view(), name='delete_stream')
]
