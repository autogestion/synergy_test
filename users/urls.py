from django.conf.urls import patterns, url
from .views import UserListView, UserOperationView

urlpatterns = patterns('',
    url(r'^$', UserListView.as_view(), name='users'),
    url(r'^edit/', UserOperationView.as_view(), name='edit'),
)
