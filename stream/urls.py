from django.urls import path
from . import views

app_name = 'stream'
urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
]