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
import logging
import base64
import os
import json
logger = logging.getLogger(__name__)

# Create your views here.

def postItem(request):
    print 'request info: %s %s' % (request.method, request.path)
    try:
        result = {}
        errors=[]
        title = None
        feature = None
        price = None
        oldPrice = None
        postUsername = None
        mobile = None
        styleIndex = 1
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
            postUsername = request.POST.get('name')
            mobile = request.POST.get('mobile')
            description = request.POST.get('description')
            if request.POST.get('type'):
                styleIndex = request.POST.get('type')
                print 'style %s' % styleIndex
            files = request.FILES.getlist('upfile[]')
            print 'title: %s name: %s description: %s' %(title, postUsername,description)
            SessionId = os.urandom(10)
            for fileEach in files:
                result = uploadImage(fileEach,SessionId)
                if result['status'] == 200:
                    imageUrls.append(result['ImageUrl'])
                else:
                    return render_to_response('pub_1.html')
            itemid = user_items_table.createUniqueItemId()
            itemObject = user_items_table.objects.create(ItemId=itemid,ItemName=title,ItemOldPrice=oldPrice,ItemPrice=price,ItemImageUrls=imageUrls,ItemType=styleIndex,TzyUser=user)
            itemObject.PostTime = createdTime
            itemObject.LastEditTime = createdTime
            itemObject.ItemDescription = description
            itemObject.save() 

    except Exception as e:
        logger.debug('upload-image: %s' % e)
        return render_to_response('pub_1.html')
    return render_to_response('pub_2.html')

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