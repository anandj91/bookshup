from django.conf.urls import patterns, include, urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookshup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', include('login.urls')),
)
