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
from application.display_items.models import comments_table
from django.http import HttpResponseRedirect
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
            itemObject.ContactUserName = contactUsername
            itemObject.ContactUserPhone = mobile
            itemObject.save() 
            return render_to_response('pub_2.html',{"type":typeIndex})

    except Exception as e:
        logger.debug('postItem: %s' % e)
        
    return render_to_response('pub_1.html')

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
        createdTime = getCurrentTime()
        description = ""
        if request.method == "POST":
            title = request.POST.get('title')
            contactUsername = request.POST.get('name')
            mobile = request.POST.get('mobile')
            description = request.POST.get('description')
            itemid = ask_info_table.createUniqueItemId()
            itemObject = ask_info_table.objects.create(ItemId=itemid,ItemTitle=title)
            if request.user.is_authenticated():
                itemObject.TzyUser = request.user
            itemObject.PostTime = createdTime
            itemObject.ItemDescription = description
            itemObject.ContactUsername = contactUsername
            itemObject.ContactUserPhone = mobile
            itemObject.save() 
            return HttpResponseRedirect("/index.html")

    except Exception as e:
        logger.debug('postAskInfo: %s' % e)
        
    return HttpResponseRedirect("/ask_item.html")

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
        items_sets = ask_info_table.objects.exclude(IsBlock=True).order_by('-PostTime')[:3]
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

def getEssenceBooks(request):
    result = {}
    essence_list = []
    pagenum = 1
    continuationToken = False
    try:
        user_ssl = tzy_users.objects.filter(username="尚书林")

        #pagenum
        req = json.loads(request.body)
        if req.has_key('pagenum'):
            pagenum = req['pagenum']
            if pagenum <= 0:
                pagenum = 1

        # essence items
        start_index = (pagenum-1)*6
        end_index = pagenum*6
        hot_sets = user_items_table.objects.filter(TzyUser=user_ssl).order_by('-ClickCount','-PostTime')[start_index:end_index]
        if  hot_sets.exists():
            for item in  hot_sets.iterator():
                image_urls = json.loads(item.ItemImageUrls)
                essence_list.append({
                    "ItemId":item.ItemId,
                    "Title":item.ItemName,
                    "Price":item.ItemPrice,
                    "OldPrice":item.ItemOldPrice,
                    "ImageUrl":image_urls[0],
                    "Description":item.ItemDescription,
                })
        if len(essence_list) == 6:
            continuationToken = True
    except Exception as e:
        logger.debug('getEssenceBooks: %s' % e)

    result["book_list"] = essence_list
    result["continuationToken"] = continuationToken
    return handle_response(result)

def getSSLEnBooks(request):
    en_result = []
    try:    
        # en items ,ItemType="100"
        en_result = getBooksWithType("")
    except Exception as e:
        logger.debug('getSSLEnBooks: %s' % e)
    
    return handle_response(en_result)

def getSSLMaPhBooks(request):
    maph_result = []
    try:    
        maph_result = getBooksWithType("")
    except Exception as e:
        logger.debug('getSSLMaPhBooks: %s' % e)

    return handle_response(maph_result)

def getBooksWithType(typeStr):
    try:
        result = [];
        user_ssl = tzy_users.objects.filter(username="尚书林")
        if typeStr == "":
            book_sets = user_items_table.objects.filter(TzyUser=user_ssl).order_by('-ClickCount','-PostTime')[:12]
        else:
            book_sets = user_items_table.objects.filter(TzyUser=user_ssl,ItemType=typeStr).order_by('-ClickCount','-PostTime')[:12]
        if  book_sets.exists():
            for item in  book_sets.iterator():
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
        logger.debug('getBooksWithType: %s' % e)

    return result

def openItem(request):
    print 'request info: %s %s' % (request.method, request.path)
    itemid = ""
    result = {}
    login_user = None
    is_owner = False
    try:
        if request.method == "GET":
            if request.user.is_authenticated():
                login_user = request.user
                result["Username"]=login_user
            itemid = request.GET.get("id")
            item_sets = user_items_table.objects.filter(ItemId=itemid)
            if  item_sets.exists():
                item = item_sets[0]
                item.clickAction()
                postUser = item.TzyUser
                is_owner = login_user == postUser
                image_urls = json.loads(item.ItemImageUrls)
                result["ItemId"]= item.ItemId
                result["Title"]= item.ItemName
                result["Price"]= item.ItemPrice
                result["OldPrice"]=item.ItemOldPrice
                result["ImageUrls"]=image_urls
                result["Description"]=item.ItemDescription
                result["ClickCount"] = item.ClickCount
                result["PostTime"] = formatTime(item.PostTime,"%Y-%m-%d %H:%M")
                result["LastEditTime"] = formatTime(item.LastEditTime,"%Y-%m-%d %H:%M")
                result["Feature"] = item.Feature
                result["IsOwner"] = is_owner
                result["ContactUserName"] = item.ContactUserName
                result["UserDisplayPhone"] = item.ContactUserPhone[:7]
                result["ContactUserPhone"] = item.ContactUserPhone
                result["QQ"] = postUser.QQ
                result["PostUserName"] = postUser.username
                user_post_sets = user_items_table.objects.filter(TzyUser=postUser)
                result["UserPostCount"] = len(user_post_sets)
                result["ReceiveCommentCount"] = len(comments_table.objects.filter(ItemPostUsername=postUser.username))
                result["SuccessDeal"] = len(user_post_sets.filter(IsTradeSuccess=True))
                return render_to_response('open_item.html',{"result":result})

    except Exception as e:
        logger.debug('openItem: %s' % e)

    return HttpResponseRedirect("/index.html")

def getAllPostsForUser(request):
    result = []
    username = ""
    postUser = None
    try:
        req = json.loads(request.body)
        if req.has_key('username'):
            username = req['username']
            postUser_set = tzy_users.objects.filter(username=username)
            if postUser_set.exists():
                postUser = postUser_set[0]
                if req.has_key('is_trade_success'):
                    item_sets =  user_items_table.objects.filter(TzyUser=postUser,IsTradeSuccess=True).order_by('-ClickCount','-PostTime')[:5]
                else:
                    item_sets =  user_items_table.objects.filter(TzyUser=postUser).order_by('-ClickCount','-PostTime')[:5]
                if  item_sets.exists():
                    for item in  item_sets.iterator():
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
        logger.debug('getAllPostsForUser: %s' % e)

    return handle_response(result)