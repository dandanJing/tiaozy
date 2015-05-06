from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tiaozy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^upload-image','application.display_items.views.uploadImage',name='uploadImage'),
    url(r'^post-item/','application.display_items.views.postItem',name='postItem'),
    url(r'^post-ask-info/','application.display_items.views.postAskInfo',name='postAskInfo'),
    url(r'^open_item','application.display_items.views.openItem',name='openItem'),
    url(r'^get-user-all-posts','application.display_items.views.getAllPostsForUser',name='getAllPostsForUser'),
    url(r'^get-my-posts-by-type','application.display_items.views.getMyPostsByType',name='getMyPostsByType'),
    url(r'^post-item-message','application.display_items.views.postItemMessage',name='postItemMessage'),
    url(r'^get-item-messages','application.display_items.views.getItemMessages',name='getItemMessages'),
    url(r'^delete-my-post-by-itemid','application.display_items.views.deleteMyPostByItemId',name='deleteMyPostByItemId'),
    url(r'^set-trade-success-by-itemid','application.display_items.views.setTradeSuccessByItemId',name='setTradeSuccessByItemId'),
    url(r'^modify-my-item','application.display_items.views.modifyMyItemByItemId',name='modifyMyItemByItemId'),
    url(r'^modify-item-type','application.display_items.views.modifyItemType',name="modifyItemType"),
    url(r'^modify-item-info','application.display_items.views.modifyItemInfo',name="modifyItemInfo"),
    url(r'^get-my-ask-items','application.display_items.views.getMyAskItems',name="getMyAskItems"),
    url(r'^delete-my-ask-by-itemid','application.display_items.views.deleteMyAskByItemId',name="deleteMyAskByItemId"),

    url(r'^get-on-selling','application.display_items.homepage.getOnSelling',name='getOnSelling'),
    url(r'^get-on-asking','application.display_items.homepage.getOnAsking',name='getOnAsking'),
    url(r'^get-ssl-essence-books','application.display_items.homepage.getEssenceBooks',name='getEssenceBooks'),
    url(r'^get-ssl-en-books','application.display_items.homepage.getSSLEnBooks',name='getSSLEnBooks'),
    url(r'^get-ssl-maph-books','application.display_items.homepage.getSSLMaPhBooks',name='getSSLMaPhBooks'),
    url(r'^get-ssl-eecp-books','application.display_items.homepage.getSSLEecpBooks',name='getSSLEecpBooks'),
    url(r'^get-ssl-soc-books','application.display_items.homepage.getSSLSocBooks',name='getSSLSocBooks'),
    url(r'^get-ssl-ec-books','application.display_items.homepage.getSSLEcBooks',name='getSSLEcBooks'),
    url(r'^get-ssl-art-books','application.display_items.homepage.getSSLArtBooks',name='getSSLArtBooks'),
)
