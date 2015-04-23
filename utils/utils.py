#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
import hashlib
import base64
import random
import string
import sys
import math
from .colors import *
from django.http import HttpResponse
import re

def md5HashEncode(string):
    string = string.encode("utf-8")
    return hashlib.md5(string).hexdigest().lower()

def md5HashEncodeWithTime(string):
    string = string.encode("utf-8")
    string += '&time=' + str(getCurrentTime())
    return hashlib.md5(string).hexdigest().lower()

def sha1HashAndBase64Encode(string):
    string = string.encode("utf-8")
    digest = hashlib.sha1(string).digest()
    sha1andbase64 = base64.b64encode(digest)
    return sha1andbase64

def base64Encode(string):
    string = string.encode("utf-8")
    return base64.b64encode(string)

def base64Decode(string):
    string = string.encode("utf-8")
    return base64.b64decode(string)

def json_dumps(json_obj):
    string = json.dumps(json_obj)
    return string

def json_loads(string):
    try:
        json_obj = json.loads(string)
    except ValueError:
        return None
    else:
        return json_obj

def getCurrentTime():
    return int(time.time())

def formatTime(input_time,time_format):
    try:
        timeArray = time.localtime(input_time)
        formatTime =  time.strftime(time_format,timeArray)
    except ValueError:
        return None
    else:
        return formatTime

def dict_extend(dict_obj, extend):
    for key in extend:
        dict_obj[key] = extend[key]
    return dict_obj

def getRandomString(length=32):
    return ''.join(random.sample(string.ascii_letters + string.digits, length)).lower()

def getRandomLetter(length=6):
    return ''.join(random.sample(string.ascii_letters, length)).upper()

def getRandomNumber(length=6):
    return ''.join(random.sample(string.digits, length))

def str2sec(string, format='%Y-%m-%d %H:%M:%S'):
    return int(time.mktime(time.strptime(string, format)))

def sec2str(second, format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format, time.localtime(second))

def getPrefix(string, length=20):
    return '%s...' % string[:length] if len(string) > length else string

def getDistanceByLatAndLng(lat1, lng1, lat2, lng2, kilometer=False):
    lat1 = math.radians(lat1)
    lng1 = math.radians(lng1)
    lat2 = math.radians(lat2)
    lng2 = math.radians(lng2)
    dlng = lng2 - lng1
    dlat = lat2 - lat1
    c = (math.sin(dlat/2))**2 + math.cos(lat1) * math.cos(lat2) * (math.sin(dlng/2.0))**2
    return 2.0 * math.atan2(math.sqrt(c), math.sqrt(1.0-c)) * (6378.137 if kilometer else 6378137)

def log_request(request, logger):
    logger.info('%s %s', green('%s %s %s %s') % (request.META.get('HTTP_X_CLIENT', 'Non-Client'), request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR')), request.method, request.path), yellow(request.body))

def handle_response(content, response_msg='', logger=None, status_code=200, exception=None):
    response = HttpResponse(json_dumps(content), content_type='application/json; charset=utf-8', status=status_code)
    response['Message'] = base64.b64encode(response_msg)
    if logger:
        logger.error(red('%s%s'), response_msg, ': [%d] %s' % (sys.exc_info()[2].tb_lineno, exception) if exception else '')
    return response

def validateEmail(email):

    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
    return False