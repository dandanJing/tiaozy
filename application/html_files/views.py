#encoding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from application.ssl_users.models import tzy_users
from application.ssl_users.models import user_items_table
import logging
import json
logger = logging.getLogger(__name__)
from application.config.globals import *

# Create your views here.
def index(request):
    hot_result = []
    en_result = []
    login_user = None
    try:
        if not request.user.is_authenticated():
            auth.logout(request)
        else:
            login_user = request.user
        user_ssl = tzy_users.objects.filter(username="尚书林")

        # essence items
        hot_sets = user_items_table.objects.filter(TzyUser=user_ssl).order_by('-ClickCount','-PostTime')[:6]
        if  hot_sets.exists():
            for item in  hot_sets.iterator():
                image_urls = json.loads(item.ItemImageUrls)
                hot_result.append({
                    "ItemId":item.ItemId,
                    "Title":item.ItemName,
                    "Price":item.ItemPrice,
                    "OldPrice":item.ItemOldPrice,
                    "ImageUrl":image_urls[0],
                    "Description":item.ItemDescription,
                })

        # en items
        en_sets = user_items_table.objects.filter(TzyUser=user_ssl,ItemType="100").order_by('-ClickCount','-PostTime')[:6]
        if  en_sets.exists():
            for item in  en_sets.iterator():
                image_urls = json.loads(item.ItemImageUrls)
                en_result.append({
                    "ItemId":item.ItemId,
                    "Title":item.ItemName,
                    "Price":item.ItemPrice,
                    "OldPrice":item.ItemOldPrice,
                    "ImageUrl":image_urls[0],
                    "Description":item.ItemDescription,
                })
    except Exception as e:
        logger.debug('pub_1: %s' % e)
    
    return render_to_response('index.html',{'login_user':login_user,"essence_items":hot_result,'en_items':en_result})
    

def publish(request):
    if request.user.is_authenticated():
        return render_to_response('publish.html')
    else:
        return render_to_response("login.html")

def pub_1(request):
    typeIndex = 101
    typeStr = ""
    username = None
    mobile = None
    if not request.user.is_authenticated():
        return render_to_response("login.html")
    try:
        if request.method == "GET":
            typeIndex = request.GET.get('type')
            typeStr = TYPEDIC[str(typeIndex)]
            print "select typeStr:  %s" % typeStr
        username =  request.user.username
        mobile = request.user.Mobilephone
    except Exception as e:
        logger.debug('pub_1: %s' % e)
    # print 'type: %s'%(typeIndex)
    return render_to_response('pub_1.html',{'typeIndex':typeIndex,'username':username,'mobile':mobile,"typeStr":typeStr})

def askItem(request):
    username = None
    mobile = None
    try:
        if request.user.is_authenticated():
            username =  request.user.username
            mobile = request.user.Mobilephone
    except Exception as e:
        logger.debug('askItem: %s' % e)
    return render_to_response('ask_item.html',{'username':username,'mobile':mobile})