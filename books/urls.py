from django.conf.urls import patterns, url

from books import views

urlpatterns = patterns('',
		url(r'^$', views.search_books, name='search_books'),
    url(r'^categories$', views.get_categories, name='get_categories'),
)