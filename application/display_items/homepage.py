# -*- coding: utf-8 -*-
from django.shortcuts import render
from utils.utils import *
from application.config.globals import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from application.ssl_users.models import user_items_table
from application.ssl_users.models import tzy_users
from application.display_items.models import ask_info_table
from application.display_items.models import comments_table
from application.display_items.models import item_messages_table
import logging
import base64
import os
import json
import math
logger = logging.getLogger(__name__)


def getOnSelling(request):
    print 'request info: %s %s' % (request.method, request.path)
    try:
        result = []
        if user_items_table.objects.exclude(IsBlock=True).count() > 2:
            items_sets = user_items_table.objects.exclude(IsBlock=True).order_by('-PostTime')[:3]
        else:
            items_sets = user_items_table.objects.exclude(IsBlock=True).order_by('-PostTime')
        #print items_sets
        if items_sets.exists():
            for item in items_sets.iterator():
                image_urls = json.loads(item.ItemImageUrls)
                if len(image_urls) > 0:                    
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
        logger.debug('getOnSelling: %s' % e)

    return handle_response(result)

def getOnAsking(request):
    print 'request info: %s %s' % (request.method, request.path)
    try:
        result = []
        if ask_info_table.objects.exclude(IsBlock=True).count() > 2:
            items_sets = ask_info_table.objects.exclude(IsBlock=True).order_by('-PostTime')[:3]
        else:
            items_sets = ask_info_table.objects.exclude(IsBlock=True).order_by('-PostTime')
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
    print "getEssenceBooks"
    try:
        user_ssl_sets = tzy_users.objects.filter(username="尚书林")
        if user_ssl_sets.exists():
            user_ssl = user_ssl_sets[0]
            #pagenum
            req = json.loads(request.body)
            if req.has_key('pagenum'):
                pagenum = req['pagenum']
                if pagenum <= 0:
                    pagenum = 1

            # essence items
            start_index = (pagenum-1)*6
            end_index = pagenum*6
            total_num = user_items_table.objects.filter(TzyUser=user_ssl).order_by('-ClickCount','-PostTime').count()
            if  total_num >= end_index:
                hot_sets = user_items_table.objects.filter(TzyUser=user_ssl).order_by('-ClickCount','-PostTime')[start_index:end_index]
            elif total_num > start_index:
                hot_sets = user_items_table.objects.filter(TzyUser=user_ssl).order_by('-ClickCount','-PostTime')[start_index:]
            else:
                result["book_list"] = essence_list
                result["continuationToken"] = continuationToken
                return handle_response(result)  
            if  hot_sets.exists():
                for item in  hot_sets.iterator():
                    image_urls = json.loads(item.ItemImageUrls)
                    if len(image_urls):             
                        imageUrl = image_urls[0]
                    else:
                        imageUrl = ""
                    essence_list.append({
                        "ItemId":item.ItemId,
                        "Title":item.ItemName,
                        "Price":item.ItemPrice,
                        "OldPrice":item.ItemOldPrice,
                        "ImageUrl":imageUrl,
                        "Description":item.ItemDescription,
                    })
            if len(essence_list) == 6:
                continuationToken = True
    except Exception as e:
        logger.debug('getEssenceBooks: %s' % e)

    #print essence_list
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

def getSSLEecpBooks(request):
    eecp_result = []
    try:    
        eecp_result = getBooksWithType("102")
    except Exception as e:
        logger.debug('getSSLEecpBooks: %s' % e)

    return handle_response(eecp_result)

def getSSLSocBooks(request):
    soc_result = []
    try:    
        soc_result = getBooksWithType("103")
    except Exception as e:
        logger.debug('getSSLSocBooks: %s' % e)

    return handle_response(soc_result)

def getSSLEcBooks(request):
    ec_result = []
    try:    
        ec_result = getBooksWithType("104")
    except Exception as e:
        logger.debug('getSSLEcBooks: %s' % e)

    return handle_response(ec_result)

def getSSLArtBooks(request):
    art_result = []
    try:    
        art_result = getBooksWithType("105")
    except Exception as e:
        logger.debug('getSSLArtBooks: %s' % e)

    return handle_response(art_result)

def getBooksWithType(typeStr):
    try:
        result = [];
        user_ssl = tzy_users.objects.filter(username="尚书林")
        if typeStr == "":
            if user_items_table.objects.filter(TzyUser=user_ssl).count()>=12:
                book_sets = user_items_table.objects.filter(TzyUser=user_ssl).order_by('-ClickCount','-PostTime')[:12]
            else:
                book_sets = user_items_table.objects.filter(TzyUser=user_ssl).order_by('-ClickCount','-PostTime')
        else:
            if user_items_table.objects.filter(TzyUser=user_ssl,ItemType=typeStr).count()>=12:
                book_sets = user_items_table.objects.filter(TzyUser=user_ssl,ItemType=typeStr).order_by('-ClickCount','-PostTime')[:12]
            else:
                book_sets = user_items_table.objects.filter(TzyUser=user_ssl,ItemType=typeStr).order_by('-ClickCount','-PostTime')
        if  book_sets.exists():
            for item in  book_sets.iterator():
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
        logger.debug('getBooksWithType: %s' % e)

    return result