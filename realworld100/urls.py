from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url('^$', 'filechecker.views.index'),
)
