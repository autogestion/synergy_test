from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', "users.views.index", name='users'),
)
