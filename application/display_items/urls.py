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
    url(r'^get-ssl-eecp-books','application.display_items.views.getSSLEecpBooks',name='getSSLEecpBooks'),
    url(r'^get-ssl-soc-books','application.display_items.views.getSSLSocBooks',name='getSSLSocBooks'),
    url(r'^get-ssl-ec-books','application.display_items.views.getSSLEcBooks',name='getSSLEcBooks'),
    url(r'^get-ssl-art-books','application.display_items.views.getSSLArtBooks',name='getSSLArtBooks'),
    url(r'^open_item','application.display_items.views.openItem',name='openItem'),
    url(r'^get-user-all-posts','application.display_items.views.getAllPostsForUser',name='getAllPostsForUser'),
    url(r'^get-my-posts-by-type','application.display_items.views.getMyPostsByType',name='getMyPostsByType'),
    url(r'^post-item-message','application.display_items.views.postItemMessage',name='postItemMessage'),
    url(r'^get-item-messages','application.display_items.views.getItemMessages',name='getItemMessages'),
)
