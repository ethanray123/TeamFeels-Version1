from django.urls import path
from .views import HomeView, UserFormView, LobbyView, \
    StreamerView, subscribe, SearchView, report, CommentView


app_name = 'stream'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', UserFormView.as_view(), name='register'),
    path('lobby/<int:pk>', LobbyView.as_view(),
         name='lobby-detail'),
    path('streamer/<int:pk>', StreamerView.as_view(),
         name='streamer-detail'),
    path('subscribe/<int:streamer_id>/<int:lobby_id>',
         subscribe, name='subscribe'),
    path('report/<int:streamer_id>', report, name='report'),
    path('search_result/', SearchView.as_view(), name='search_view'),
    path('lobby/comments/',
         CommentView.as_view(), name='comment_view')
]

# path('', views.HomeView.as_view(), name='home'),
# path('register/', views.UserFormView.as_view(), name='register'),
# path('lobby/<int:pk>', views.LobbyView.as_view(),
#      name='lobby-detail'),
# not implemented yet:
