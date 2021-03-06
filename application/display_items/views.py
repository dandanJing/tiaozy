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
from application.display_items.models import item_messages_table
from django.http import HttpResponseRedirect
import logging
import base64
import os
import json
import math
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
                feature = '1'
            else:
                feature = '0'
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
            print 'title: %s name: %s' %(title, postUsername)
            SessionId = os.urandom(10)
            #print request.FILES
            for fileEach in files:
                result = uploadImage(fileEach,SessionId)
                print result
                if result['status'] == 200:
                    imageUrls.append(result['ImageUrl'])
                else:
                    return render_to_response('pub_1.html')
            itemid = user_items_table.createUniqueItemId()
            itemObject = user_items_table.objects.create(ItemId=itemid,ItemName=title,ItemOldPrice=oldPrice,ItemPrice=price,ItemImageUrls=json.dumps(imageUrls),ItemType=typeIndex,TzyUser=user)
            itemObject.PostTime = createdTime
            itemObject.LastEditTime = createdTime
            if description != None:
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
            #print res.status
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
            itemObject.LastEditTime = itemObject.PostTime
            itemObject.ItemDescription = description
            itemObject.ContactUserName = contactUsername
            itemObject.ContactUserPhone = mobile
            itemObject.save() 
            return HttpResponseRedirect("/index.html")

    except Exception as e:
        logger.debug('postAskInfo: %s' % e)
        
    return HttpResponseRedirect("/ask_item.html")

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
                result["MessageCount"] = len(item_messages_table.objects.filter(Item=item))
                pagenum = int(math.ceil(float(result["MessageCount"])/MESSAGES_PER_PAGE))
                if pagenum > 1:
                    result["MessagePageIndexs"] = range(1,pagenum+1)
                return render_to_response('open_item.html',{"result":result})

    except Exception as e:
        logger.debug('openItem: %s' % e)

    return HttpResponseRedirect("/index.html")

def getAllPostsForUser(request):
    print 'request info: %s %s' % (request.method, request.path)
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
                    if user_items_table.objects.filter(TzyUser=postUser,IsTradeSuccess=True).count()>=5:
                        item_sets =  user_items_table.objects.filter(TzyUser=postUser,IsTradeSuccess=True).order_by('-ClickCount','-PostTime')[:5]
                    else:
                        item_sets =  user_items_table.objects.filter(TzyUser=postUser,IsTradeSuccess=True).order_by('-ClickCount','-PostTime')
                else:
                    if user_items_table.objects.filter(TzyUser=postUser).order_by('-ClickCount','-PostTime').count()>=5:
                        item_sets =  user_items_table.objects.filter(TzyUser=postUser).order_by('-ClickCount','-PostTime')[:5]
                    else:
                        item_sets =  user_items_table.objects.filter(TzyUser=postUser).order_by('-ClickCount','-PostTime')
                if  item_sets.exists():
                    for item in  item_sets.iterator():
                        image_urls = json.loads(item.ItemImageUrls)
                        if len(image_urls):             
                            imageUrl = image_urls[0]
                        else:
                            imageUrl = ""
                        result.append({
                            "ItemId":item.ItemId,
                            "Title":item.ItemName,
                            "Price":item.ItemPrice,
                            "OldPrice":item.ItemOldPrice,
                            "ImageUrl":imageUrl,
                            "Description":item.ItemDescription,
                        })

    except Exception as e:
        logger.debug('getAllPostsForUser: %s' % e)

    return handle_response(result)

def getMyPostsByType(request):
    print 'request info: %s %s' % (request.method, request.path)
    result = []
    username = ""
    postUser = None
    getpage = 1
    try:
        req = json.loads(request.body)
        if request.user.is_authenticated():
            username = request.user.username
            postUser_set = tzy_users.objects.filter(username=username)
            if postUser_set.exists():
                postUser = postUser_set[0]
                typeStr = "all"
                num = user_items_table.objects.exclude(IsDelete=True).filter(TzyUser=postUser).count()
                pagenum = int(math.ceil(float(num)/ITEMS_PER_PAGE_FOR_MYCENTER))
                if req.has_key('getPage'):
                    getpage = int(req['getPage'])
                start_index = ITEMS_PER_PAGE_FOR_MYCENTER*(getpage-1)
                end_index = ITEMS_PER_PAGE_FOR_MYCENTER*getpage
                if req.has_key('type'):
                    typeStr = req['type']
                    if typeStr == "time":
                        item_sets =  user_items_table.objects.exclude(IsDelete=True).filter(TzyUser=postUser).order_by('-PostTime')[start_index:end_index]
                    elif typeStr == "click":
                        item_sets =  user_items_table.objects.exclude(IsDelete=True).filter(TzyUser=postUser).order_by('-ClickCount')[start_index:end_index]
                    elif typeStr == "success":
                        item_sets =  user_items_table.objects.exclude(IsDelete=True).filter(TzyUser=postUser,IsTradeSuccess=True)[start_index:end_index]
                        num = user_items_table.objects.exclude(IsDelete=True).filter(TzyUser=postUser,IsTradeSuccess=True).count()
                        pagenum = int(math.ceil(float(num)/ITEMS_PER_PAGE_FOR_MYCENTER))
                    else:
                        item_sets =  user_items_table.objects.exclude(IsDelete=True).filter(TzyUser=postUser)[start_index:end_index]
                else:
                    item_sets =  user_items_table.objects.exclude(IsDelete=True).filter(TzyUser=postUser)[start_index:end_index]
                if  item_sets.exists():
                    for item in  item_sets.iterator():
                        message_count = item_messages_table.objects.filter(Item=item).count()
                        image_urls = json.loads(item.ItemImageUrls)
                        if len(image_urls):             
                            imageUrl = image_urls[0]
                        else:
                            imageUrl = ""
                        result.append({
                            "ItemId":item.ItemId,
                            "Title":item.ItemName,
                            "Price":item.ItemPrice,
                            "OldPrice":item.ItemOldPrice,
                            "ImageUrl":imageUrl,
                            "Description":item.ItemDescription,
                            "PostTime":formatTime(item.PostTime,"%Y-%m-%d %H:%M"),
                            "IsTradeSuccess":item.IsTradeSuccess,
                            "ClickCount":item.ClickCount,
                            "MessageCount":message_count,
                        })

    except Exception as e:
        logger.debug('getMyPostsByType: %s' % e)

    for_result = {"result":result,"Pagenum":range(1,pagenum+1),}
    return handle_response(for_result)

def deleteMyPostByItemId(request):
    result = {}
    result['result']=False
    itemid = ""
    try:
        req = json.loads(request.body)
        if request.user.is_authenticated():
            if req.has_key('itemid'):
                itemid = req['itemid']
                if user_items_table.objects.filter(ItemId=itemid).count() > 0:
                    item = user_items_table.objects.get(ItemId=itemid)
                    if item.TzyUser == request.user:
                        item.IsDelete = True
                        item.save()
                        result['result']=True
                
    except Exception as e:
        logger.debug('deleteMyPostByItemId: %s' % e)  

    return handle_response(result)     

def setTradeSuccessByItemId(request):
    result={}
    result['result']=False
    itemid = ""
    try:
        req = json.loads(request.body)
        if request.user.is_authenticated():
            if req.has_key('itemid'):
                itemid = req['itemid']
                if user_items_table.objects.filter(ItemId=itemid).count() > 0:
                    item = user_items_table.objects.get(ItemId=itemid)
                    if item.TzyUser == request.user:
                        item.IsTradeSuccess = True
                        item.save()
                        result['result']=True
                
    except Exception as e:
        logger.debug('setTradeSuccessByItemId: %s' % e)  

    return handle_response(result)

def modifyMyItemByItemId(request):
    print 'request info: %s %s' % (request.method, request.path)
    result = {}
    typeStr = ""
    try:
        if request.method == "GET":
            if request.user.is_authenticated(): 
                itemid = request.GET.get("itemid")
                item_sets = user_items_table.objects.filter(ItemId=itemid)
                if  item_sets.exists():
                    item = item_sets[0]
                    if item.TzyUser == request.user:
                        image_urls = json.loads(item.ItemImageUrls)
                        typeIndex = item.ItemType
                        typeStr = TYPEDIC[str(typeIndex)]
                        feature = 0
                        if item.Feature == "全新":
                            feature = 1
                        result = {
                            "ItemId":item.ItemId,
                            "Title":item.ItemName,
                            "Feature":feature,
                            "Price":item.ItemPrice,
                            "OldPrice":item.ItemOldPrice,
                            "ImageUrls":image_urls,
                            "Description":item.ItemDescription,
                            "PostTime":formatTime(item.PostTime,"%Y-%m-%d %H:%M"),
                            "IsTradeSuccess":item.IsTradeSuccess,
                            'ContactUserPhone':item.ContactUserPhone,
                            'ContactUserName':item.ContactUserName,
                        }
                        return render_to_response('modify_item_info.html',{"item":result,"typeStr":typeStr})
    except Exception as e:
        logger.debug('modifyMyItemByItemId: %s' % e)

    return HttpResponseRedirect("/index.html")

def modifyItemType(request):
    itemid = ""
    typeIndex = '100'
    try:
        if request.method == "GET":
            if request.user.is_authenticated(): 
                itemid = request.GET.get("itemid")
                typeIndex = request.GET.get("type")
                item = user_items_table.objects.get(ItemId=itemid)
                if item and item.TzyUser == request.user:
                    item.ItemType = typeIndex
                    item.LastEditTime = getCurrentTime()
                    item.save()
                    return modifyMyItemByItemId(request)
    except Exception as e:
        logger.debug('modifyItemType: %s' % e)

    return HttpResponseRedirect("/index.html")

def modifyItemInfo(request):
    itemid = ""
    try:
        if request.method == "POST" and request.user.is_authenticated():
            itemid = request.GET.get("itemid")
            item = user_items_table.objects.get(ItemId=itemid)
            if item and item.TzyUser == request.user:
                title = request.POST.get('title')
                temp = request.POST.get('feature')
                print temp
                if temp == '1':
                    feature = '全新'
                else:
                    feature = '非全新'
                oldPrice = request.POST.get('original-price')
                price = request.POST.get('price')
                contactUsername = request.POST.get('name')
                mobile = request.POST.get('mobile')
                description = request.POST.get('description')
                if title != item.ItemName:
                    item.ItemName = title
                if feature != item.Feature:
                    item.Feature = feature
                if oldPrice != item.ItemOldPrice:
                    item.ItemOldPrice = oldPrice
                if price != item.ItemPrice:
                    item.ItemPrice = price
                if contactUsername != item.ContactUserName:
                    item.ContactUserName = contactUsername
                if mobile != item.ContactUserPhone:
                    item.ContactUserPhone = mobile
                if description != item.ItemDescription:
                    item.ItemDescription = description
                item.LastEditTime = getCurrentTime()
                item.save()
                return render_to_response('modify_item_success.html',{'ItemId':itemid})
    except Exception as e:
        logger.debug('modifyItemInfo: %s' % e)

    return HttpResponseRedirect("/index.html")

def modifyAskInfo(request):
    try:
        if request.method == "POST" and request.user.is_authenticated():
            itemid = request.GET.get("itemid")
            item = ask_info_table.objects.get(ItemId=itemid)
            if item and item.TzyUser == request.user:
                title = request.POST.get('title')
                mobile = request.POST.get('mobile')
                contactUsername = request.POST.get('name')
                description = request.POST.get('description')
                if title != item.ItemTitle:
                    item.ItemTitle = title
                if mobile != item.ContactUserPhone:
                    item.ContactUserPhone = mobile
                if contactUsername != item.ContactUserName:
                    item.ContactUserName = contactUsername
                if description != item.ItemDescription:
                    item.ItemDescription = description
                item.LastEditTime = getCurrentTime()
                item.save()
                return HttpResponseRedirect("/open-my-center/")
    except Exception as e:
        logger.debug('modifyAskInfo: %s' % e)

    return HttpResponseRedirect("/index.html")

def postItemMessage(request):
    result = []
    itemid = None
    message = ""
    try:
        req = json.loads(request.body)
        if req.has_key('itemid'):
            itemid = req["itemid"]
        if req.has_key('message'):
            message = req["message"]
        item_sets =  user_items_table.objects.filter(ItemId=itemid)
        if  item_sets.exists():
            item = item_sets[0]
            messageId = item_messages_table.createUniqueMessageId()
            msgObject = item_messages_table.objects.create(MessageId=messageId,Message=message,Item=item)
            msgObject.PostTime = getCurrentTime()
            message_str = message
            if request.user.is_authenticated():
                msgObject.TzyUser = request.user
                message_str = request.user.username+" : "+message
            msgObject.save()
            result.append({
                "MessageId":msgObject.MessageId,
                "Message":message_str,
                "PostTime":formatTime(msgObject.PostTime,"%Y-%m-%d %H:%M")
            })

    except Exception as e:
        logger.debug('postItemMessage: %s' % e)

    return handle_response(result)

def getItemMessages(request):
    print 'request info: %s %s' % (request.method, request.path)
    result = []
    itemid = ""
    pagenum = 1
    try:
        req = json.loads(request.body)
        if req.has_key('pagenum'):
            pagenum = req["pagenum"]
        if req.has_key('itemid'):
            itemid = req["itemid"]
            item_sets =  user_items_table.objects.filter(ItemId=itemid)
            if  item_sets.exists():
                item = item_sets[0]
                start_index = MESSAGES_PER_PAGE*(pagenum-1)
                end_index = MESSAGES_PER_PAGE*(pagenum)
                message_sets = item_messages_table.objects.filter(Item=item)[start_index:end_index]
                if message_sets.exists():
                    for message in  message_sets.iterator():
                        message_str = message.Message
                        if message.TzyUser:
                            message_str = message.TzyUser.username+" : "+message.Message
                        result.append({
                            "MessageId":message.MessageId,
                            "Message":message_str,
                            "PostTime":formatTime(message.PostTime,"%Y-%m-%d %H:%M")
                        })

    except Exception as e:
        logger.debug('getItemMessages: %s' % e)

    return handle_response(result)

def getMyAskItems(request):
    result = []
    try:
        if request.user.is_authenticated():
            item_sets = ask_info_table.objects.filter(TzyUser=request.user).exclude(IsDelete=True)
            if  item_sets.exists():
                for item in item_sets.iterator():
                    result.append({
                        "ItemId":item.ItemId,
                        "Title":item.ItemTitle,
                        "Description":item.ItemDescription,
                        "PostTime":formatTime(item.PostTime,"%Y-%m-%d %H:%M"),
                        "LastEditTime":formatTime(item.LastEditTime,"%Y-%m-%d %H:%M"),
                        "ClickCount":item.ClickCount,
                        "ContactUserName":item.ContactUserName,
                        "ContactUserPhone":item.ContactUserPhone,
                    })
    except Exception as e:
        logger.debug('getMyAskItems: %s' % e)

    return handle_response(result)

def deleteMyAskByItemId(request):
    result = {}
    result['result']=False
    itemid = ""
    try:
        req = json.loads(request.body)
        if request.user.is_authenticated():
            if req.has_key('itemid'):
                itemid = req['itemid']
                if ask_info_table.objects.filter(ItemId=itemid).count() > 0:
                    item = ask_info_table.objects.get(ItemId=itemid)
                    if item.TzyUser == request.user:
                        item.IsDelete = True
                        item.save()
                        result['result']=True
    except Exception as e:
        logger.debug('deleteMyAskByItemId: %s' % e)

    return handle_response(result)

