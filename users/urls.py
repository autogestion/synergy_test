from django.conf.urls import patterns, url
from .views import UserListView

urlpatterns = patterns('',
    url(r'^$', UserListView.as_view(), name='users'),
)
