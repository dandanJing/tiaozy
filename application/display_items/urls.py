from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tiaozy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^post-item/','application.display_items.views.postItem',name='postItem'),
    url(r'^upload-image','application.display_items.views.uploadImage',name='uploadImage'),
)
