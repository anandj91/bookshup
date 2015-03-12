from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookshup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', include('login.urls', namespace='login')),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^books/', include('books.urls', namespace='books')),
    url(r'^shop/', include('shop.urls', namespace='shop')),
)
