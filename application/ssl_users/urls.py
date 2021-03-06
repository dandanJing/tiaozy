from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tiaozy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^reg/','application.ssl_users.views.reg',name='reg'),
    url(r'^login/','application.ssl_users.views.login',name='login'),
    url(r'^reg-username/','application.ssl_users.views.regUsername',name='regUsername'),
    url(r'^reg-user-info/','application.ssl_users.views.regUserInfo',name='regUserInfo'),
    url(r'^loginAction/','application.ssl_users.views.loginAction',name='loginAction'),
    url(r'^loginout/','application.ssl_users.views.logout',name='logout'),
    url(r'^check-user','application.ssl_users.views.checkUser',name='checkUser'),
    url(r'^open-my-center/','application.ssl_users.views.openMyCenter',name='openMyCenter'),
    url(r'^get-my-personal-info','application.ssl_users.views.getMyPersonalInfo',name='getMyPersonalInfo'),
    url(r'^change-my-info','application.ssl_users.views.changeMyPersonalInfo',name='changeMyPersonalInfo'),
    url(r'^upload-my-avatar','application.ssl_users.views.uploadMyAvatar',name='uploadMyAvatar'),
)
