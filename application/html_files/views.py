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
    login_user = None
    try:
        if not request.user.is_authenticated():
            auth.logout(request)
        else:
            login_user = request.user
        
    except Exception as e:
        logger.debug('index: %s' % e)
    
    return render_to_response('index.html',{'login_user':login_user})
    
def publish(request):
    itemid = None
    result = {}
    try:
        if not request.user.is_authenticated():
            return render_to_response("login.html")
        else:
            if request.method == "GET":
                itemid = request.GET.get("itemid")
                item_sets = user_items_table.objects.filter(ItemId=itemid)
                if item_sets.exists():
                    item = item_sets[0]
                    result['ItemId']=itemid
                    result['ItemType']=item.ItemType
                    return render_to_response('modify_item_type.html',{'result':result})
            
    except Exception as e:
        logger.debug('publish: %s' % e)

    return render_to_response("publish.html")

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
            #print "select typeStr:  %s" % typeStr
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