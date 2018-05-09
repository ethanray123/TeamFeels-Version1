from django.urls import path
# from . import views
from .views import HomeView, UserFormView, LobbyView


app_name = 'stream'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', UserFormView.as_view(), name='register'),
    path('lobby/<int:pk>', LobbyView.as_view(),
         name='lobby-detail'),
]

# path('', views.HomeView.as_view(), name='home'),
# path('register/', views.UserFormView.as_view(), name='register'),
# path('lobby/<int:pk>', views.LobbyView.as_view(),
#      name='lobby-detail'),
# not implemented yet:
# path('streamer/<int:pk>', views.StreamerView.as_view(),
# name='streamer-detail'),
