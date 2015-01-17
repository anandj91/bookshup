from django.conf.urls import patterns, url

from books import views

urlpatterns = patterns('',
    url(r'^categories$', views.get_categories, name='get_categories'),
)