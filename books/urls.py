from django.conf.urls import patterns, url

from books import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
    url(r'^categories$', views.categories, name='categories'),
    url(r'^(?P<id>\d+)$', views.book, name='book'),
    url(r'^(?P<id>\d+)/sellers$', views.sellers, name='sellers'),
    url(r'^(?P<id>\d+)/comments$', views.comments, name='comments'),
)