from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tiaozy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('application.ssl_users.urls')),
    url(r'^', include('application.html_files.urls')),
    url(r'^', include('application.display_items.urls')),
    url(r'^tinymce/', include('application.tinymce.urls')),
    url(r'$','application.html_files.views.index',name='index'),
)
