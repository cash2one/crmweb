from django.conf.urls import patterns, url

urlpatterns = patterns('repository.views',
    url(r'^scan/$', 'scan', name='scan'),

)