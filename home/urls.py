from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.books, name='books'),
    url(r'^books/search/$', views.books_search, name='books_search'),
)