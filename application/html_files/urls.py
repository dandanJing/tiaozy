from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tiaozy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^publish-item/pub/','application.html_files.views.pub_1',name='pub_1'),
    url(r'^publish-item/','application.html_files.views.publishItem',name='publishItem'),
)
