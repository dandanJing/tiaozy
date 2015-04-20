from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tiaozy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^upload-image','application.display_items.views.uploadImage',name='uploadImage'),
    url(r'^post-item/','application.display_items.views.postItem',name='postItem'),
    url(r'^post-ask-info/','application.display_items.views.postAskInfo',name='postAskInfo'),
    url(r'^get-on-selling','application.display_items.views.getOnSelling',name='getOnSelling'),
)
