from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^auth$', views.auth, name='auth'),
    url(r'^logout$', views.outlog, name='logout'),
    url(r'^register$', views.register, name='register'),
)