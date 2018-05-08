from django.contrib import admin
from django.urls import path, include, re_path
from stream.views import HomeView
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('stream/', include('stream.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve,
                {'document_root': settings.MEDIA_ROOT}),
    ]
