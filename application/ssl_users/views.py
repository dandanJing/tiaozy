#encoding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from application.ssl_users.models import tzy_users
from application.display_items.views import uploadImage
from utils.utils import *
from django.http import HttpResponse
import json
from django.contrib import auth
from django.http import HttpResponseRedirect
import logging
import os
logger = logging.getLogger(__name__)

# Create your views here.
def reg(request):
    return render_to_response('reg.html')

def login(request):
    return render_to_response('login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def regUsername(request):
    errors=[]
    username = None
    phone = None
    email = None
    password = None
    cpassword = None
    try:
        if request.method == 'POST':
            if not request.POST.get('username'):
                errors.append('用户名无效')
            else:
                username = request.POST.get('username')

            if not request.POST.get('phone') and not request.POST.get('email'):
                errors.append('手机号码或邮箱有误')
            elif request.POST.get('phone'):
                phone = request.POST.get('phone')
            else:
                email = request.POST.get('email')

            if not request.POST.get('password'):
                errors.append('密码有误')
            else:
                password = request.POST.get('password')

            if not request.POST.get('cpassword'):
                errors.append('确认密码输入有误')
            else:
                cpassword = request.POST.get('cpassword')

            if username is not None and (email is not None or phone is not None)and password is not None and len(errors) == 0:
                filterResults = tzy_users.objects.filter(username=username)
                if len(filterResults)>0:
                    errors.append('用户名已存在')
                    print errors
                    return render_to_response('reg.html',{'errors':errors})
                
                filterResults = tzy_users.objects.filter(email=email)
                if len(filterResults)>0:
                    errors.append('该邮箱已注册')
                    print errors
                    return render_to_response('reg.html',{'errors':errors})

                filterResults = tzy_users.objects.filter(Mobilephone=phone)
                if len(filterResults)>0:
                    errors.append('该手机号已注册')
                    print errors
                    return render_to_response('reg.html',{'errors':errors})

                # user input verify
                user = tzy_users.objects.create_user(username=username,password=password,email=email,Nickname=username)
                if phone is not None:
                    user.Mobilephone = phone
                user.is_active = True
                user.save()
                auth_user = auth.authenticate(username=username,password=password)
                auth.login(request, auth_user)
                return render_to_response('reg.html',{'user':user})
    except Exception as e:
        logger.debug('regUsername: %s' % e)

    print errors
    return render_to_response('reg.html',{'errors':errors})

def regUserInfo(request):
    phone = None
    qq = None
    is_student = None
    errors=[]

    try:
        if request.method == 'POST':
            phone = request.POST.get('phone')
            is_student = request.POST.get('is-student')
            
            if request.user.is_authenticated():
                print request.user
                request.user.Mobilephone = phone
                if request.POST.get('qq'):
                    qq = request.POST.get('qq')
                    request.user.QQ = qq
                request.user.IsStudent = is_student
                request.user.save() 
                return render_to_response('reg.html',{'is_success':True})
    except Exception as e:
        logger.debug('regUserInfo: %s' % e)

    return render_to_response('reg.html')

def loginAction(request):
    errors = []
    user = None
    result = False

    try:
        if request.method=='POST':
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            print "login-username:"+username
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                result = True
            elif user is None:
                filterResults = tzy_users.objects.filter(Mobilephone=username)
                if len(filterResults) == 0:
                    filterResults = tzy_users.objects.filter(email=username)
                
                if len(filterResults) > 0:  
                    user = filterResults[0]       
                if user is not None and user.check_password(password) and user.is_active:
                    print user
                    user = auth.authenticate(username=user.username,password=password)
                    auth.login(request, user)
                    result = True
            if result:
                return HttpResponseRedirect("/index.html")
        errors.append('用户名或密码错误')
    except Exception as e:
        logger.debug('loginAction: %s' % e)

    return render_to_response('login.html',{"errors":errors})

def checkUser(request):
    json_data = None
    filterResults = []
    try:
        req = json.loads(request.body)
        if req.has_key('username'):
            username = req['username']
            filterResults = tzy_users.objects.filter(username=username)
        elif req.has_key('phone'):
            phone = req['phone']
            filterResults = tzy_users.objects.filter(Mobilephone=phone)
        elif req.has_key('email'):
            email = req['email']
            filterResults = tzy_users.objects.filter(email=email)

        dict1 = {}
        if len(filterResults)>0:
            dict1['code']= 200
            dict1['msg'] = False
        else:
            dict1['code']= 200
            dict1['msg'] = True
        json_data = json.dumps(dict1)
    except Exception as e:
        logger.debug('checkUser: %s' % e)

    return HttpResponse(json_data,content_type="application/json")

def openMyCenter(request):
    print 'request info: %s %s' % (request.method, request.path)
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    try:
        temp = 1
        login_user = request.user.username
        if request.GET.get('type'):
            temp = request.GET.get('type')
    except Exception as e:
        logger.debug('openMyCenter: %s' % e)

    return render_to_response('my_center.html',{"login_user":login_user,"selectType":temp})

def getMyPersonalInfo(request):
    print 'request info: %s %s' % (request.method, request.path)
    result = {}
    if not request.user.is_authenticated():
        return handle_response(result)
    else:
        try:
            result['Username'] = request.user.username
            result['Mobilephone'] = request.user.Mobilephone
            result['Email'] = request.user.email
            result['QQ'] = request.user.QQ
            result['IsStudent'] =request.user.IsStudent
            result['RealName'] = request.user.RealName
            result['AvatarUrl'] = request.user.AvatarUrl
        except Exception as e:
            logger.debug('getMyPersonalInfo: %s' % e)

    return handle_response(result)

def changeMyPersonalInfo(request):
    print 'request info: %s %s' % (request.method, request.path)
    result = {}
    phone = ""
    email = ""
    qq = ""
    realname = ""
    need_save = False
    is_student = False
    errors = []
    if not request.user.is_authenticated():
        return handle_response(result)
    else:
        try:
            if request.method == "POST":
                if request.POST.get('phone'):
                    phone = request.POST.get('phone')
                    if len(phone) != 11:
                        errors.append("手机号码输入有误")
                    elif phone != (request.user.Mobilephone):
                        request.user.Mobilephone = phone
                        need_save = True
                if request.POST.get('email'):
                    email = request.POST.get('email')
                    if not validateEmail(email):
                        errors.append("邮箱输入格式有误")
                    elif email != (request.user.email):
                        request.user.email = email
                        need_save = True
                if request.POST.get('qq'):
                    qq = request.POST.get('qq')
                    if qq != (request.user.QQ):
                        request.user.QQ = qq
                        need_save = True
                if request.POST.get('realname'):
                    realname = request.POST.get('realname')
                    if realname != (request.user.RealName):
                        request.user.RealName = realname
                        need_save = True
                if request.POST.get('is-student'):
                    is_student = int(request.POST.get('is-student'))
                    if is_student != request.user.IsStudent:
                        request.user.IsStudent = is_student
                        need_save = True
                    print "is_student : %s %d" % (request.POST.get('is-student'),is_student)
                if len(errors) > 0:
                    result["errors"] = errors
                elif need_save:
                    print "change-my-info"
                    request.user.save()
                result['Username'] = request.user.username
                result['Mobilephone'] = request.user.Mobilephone
                result['Email'] = request.user.email
                result['QQ'] = request.user.QQ
                result['IsStudent'] =request.user.IsStudent
                result['RealName'] = request.user.RealName
                result['AvatarUrl'] = request.user.AvatarUrl
        except Exception as e:
            logger.debug('changeMyPersonalInfo: %s' % e)

    return handle_response(result)

def uploadMyAvatar(request):
    print 'request info: %s %s' % (request.method, request.path)
    result = {'Status':False}
    if not request.user.is_authenticated():
        return handle_response(result)
    else:
        try:
            if request.method == "POST":
                fileObj = request.FILES.get('file')
                if fileObj:
                    SessionId = os.urandom(10)
                    result = uploadImage(fileObj,SessionId)
                    imageurl = result['ImageUrl']
                    request.user.AvatarUrl = imageurl
                    request.user.save()
                    print "imageurl : %s status %s" % (imageurl,result['status'])
                    if result['status'] == 200:
                        result['Status'] = True
                        result['AvatarUrl'] = imageurl
                else:
                    result['Status'] = True
        except Exception as e:
            logger.debug('uploadMyAvatar: %s' % e)

    print result
    return handle_response(result)