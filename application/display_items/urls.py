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
    url(r'^get-on-asking','application.display_items.views.getOnAsking',name='getOnAsking'),
    url(r'^get-ssl-essence-books','application.display_items.views.getEssenceBooks',name='getEssenceBooks'),
    url(r'^get-ssl-en-books','application.display_items.views.getSSLEnBooks',name='getSSLEnBooks'),
    url(r'^get-ssl-maph-books','application.display_items.views.getSSLMaPhBooks',name='getSSLMaPhBooks'),
)
