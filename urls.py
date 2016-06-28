from django.conf.urls import url, include
from django.contrib import admin

from users.views import UserView

urlpatterns = [
    url(r'^$', UserView.as_view(), name='users'),
    url(r'^edit/', UserView.as_view(), name='edit'),
    url(r'^admin/', include(admin.site.urls)),
]
