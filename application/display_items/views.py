# -*- coding: utf-8 -*-
from django.shortcuts import render
from oss.oss_api import *
from oss import oss_xml_handler
from utils.utils import *
from application.config.globals import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from application.ssl_users.models import user_items_table
from application.ssl_users.models import tzy_users
from application.display_items.models import ask_info_table
import logging
import base64
import os
import json
logger = logging.getLogger(__name__)

# Create your views here.

def postItem(request):
    print 'request info: %s %s' % (request.method, request.path)
    if not request.user.is_authenticated():
        return("login.html")
    try:
        result = {}
        errors=[]
        title = None
        feature = None
        price = None
        oldPrice = None
        postUsername = None
        mobile = None
        typeIndex = 1
        imageUrls = []
        user = request.user
        createdTime = getCurrentTime()
        description = ""
        if request.method == "POST":
            title = request.POST.get('title')
            temp = request.POST.get('feature')
            if temp == '1':
                feature = "全新"
            else:
                feature = "非全新"
            oldPrice = request.POST.get('original-price')
            price = request.POST.get('price')
            contactUsername = request.POST.get('name')
            mobile = request.POST.get('mobile')
            description = request.POST.get('description')
            if request.POST.get('type'):
                typeIndex = request.POST.get('type')
                # print 'select type %s' % typeIndex
            files = request.FILES.getlist('upfile[]')
            # print files
            print 'title: %s name: %s description: %s' %(title, postUsername,description)
            SessionId = os.urandom(10)
            for fileEach in files:
                result = uploadImage(fileEach,SessionId)
                print "imageurl : %s" % result['ImageUrl']
                if result['status'] == 200:
                    imageUrls.append(result['ImageUrl'])
                else:
                    return render_to_response('pub_1.html')
            itemid = user_items_table.createUniqueItemId()
            itemObject = user_items_table.objects.create(ItemId=itemid,ItemName=title,ItemOldPrice=oldPrice,ItemPrice=price,ItemImageUrls=json.dumps(imageUrls),ItemType=typeIndex,TzyUser=user)
            itemObject.PostTime = createdTime
            itemObject.LastEditTime = createdTime
            itemObject.ItemDescription = description
            itemObject.ContactUsername = contactUsername
            itemObject.ContactUserPhone = mobile
            itemObject.save() 
            return render_to_response('pub_2.html',{"type":typeIndex})

    except Exception as e:
        logger.debug('postItem: %s' % e)
        return render_to_response('pub_1.html')
    return render_to_response('index.html')

def uploadImage(image_file,SessionId):
    try:
        result = {}
        oss = OssAPI(OSS_HOST, ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        image_name = base64.urlsafe_b64encode('%s+%d' % (SessionId, getCurrentTime()))
        res = oss.put_object_from_string(OSS_BUCKET, image_name, image_file.read(), OSS_CONTENT_TYPE)
        result['status'] = res.status
        if res.status == 200:
            result['ImageUrl'] = OSS_CDN_HOST + image_name
        else:
            print res.status
            # err_msg=oss_xml_handler.ErrorXml(res.read())
            # print 'Code:'+err_msg.code
            # print 'Message:'+err_msg.msg
            # print 'Request id:'+err_msg.request_id
            result['message'] = '上传失败'
    except Exception as e:
        logger.debug('upload-image: %s' % e)

    return result

def postAskInfo(request):
    print 'request info: %s %s' % (request.method, request.path)
    try:
        result = {}
        title = None
        postUsername = None
        mobile = None
        user = request.user
        createdTime = getCurrentTime()
        description = ""
        if request.method == "POST":
            title = request.POST.get('title')
            contactUsername = request.POST.get('name')
            mobile = request.POST.get('mobile')
            description = request.POST.get('description')
            itemid = ask_info_table.createUniqueItemId()
            itemObject = ask_info_table.objects.create(ItemId=itemid,ItemTitle=title,TzyUser=user)
            itemObject.PostTime = createdTime
            itemObject.ItemDescription = description
            itemObject.ContactUsername = contactUsername
            itemObject.ContactUserPhone = mobile
            itemObject.save() 
            return render_to_response('index.html')

    except Exception as e:
        logger.debug('postAskInfo: %s' % e)
        return render_to_response('ask_item.html')
    return render_to_response('ask_item.html')

def getOnSelling(request):
    print 'request info: %s %s' % (request.method, request.path)
    try:
        result = []
        items_sets = user_items_table.objects.exclude(IsBlock=True).order_by('-PostTime')[:2]
        if items_sets.exists():
            for item in items_sets.iterator():
                image_urls = json.loads(item.ItemImageUrls)
                result.append({
                    "ItemId":item.ItemId,
                    "Title":item.ItemName,
                    "Price":item.ItemPrice,
                    "OldPrice":item.ItemOldPrice,
                    "ImageUrl":image_urls[0],
                    "Description":item.ItemDescription,
                })

    except Exception as e:
        logger.debug('getOnSelling: %s' % e)

    return handle_response(result)

def getOnAsking(request):
    print 'request info: %s %s' % (request.method, request.path)
    try:
        result = []
        items_sets = ask_info_table.objects.exclude(IsBlock=True).order_by('-PostTime')[:2]
        if items_sets.exists():
            for item in items_sets.iterator():
                result.append({
                    "ItemId":item.ItemId,
                    "Title":item.ItemTitle,
                    "Description":item.ItemDescription,
                    "PostTime":formatTime(item.PostTime,"%Y-%m-%d %H:%M")
                })

    except Exception as e:
        logger.debug('getOnAsking: %s' % e)

    return handle_response(result)