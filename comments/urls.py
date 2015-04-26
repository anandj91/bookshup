from django.conf.urls import patterns, url

from comments import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
    url(r'^book/(?P<id>\d+)$', views.book, name='book_comment'),
    url(r'^user/(?P<id>\d+)$', views.user, name='user_comment'),
)