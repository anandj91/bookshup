from django.conf.urls import patterns, url

from shop import views

urlpatterns = patterns('',
		# url(r'^$', views.index, name='index'),
		url(r'^buy$', views.buy, name='buy'),
)