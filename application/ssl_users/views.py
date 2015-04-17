#encoding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from application.ssl_users.models import tzy_users
from django.http import HttpResponse
import json
from django.contrib import auth
from django.http import HttpResponseRedirect

# Create your views here.
def reg(request):
    return render_to_response('reg.html')

def login(request):
    return render_to_response('login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index.html")

def regUsername(request):
    errors=[]
    username = None
    phone = None
    email = None
    password = None
    cpassword = None

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

            filterResults = tzy_users.objects.filter(mobilephone=phone)
            if len(filterResults)>0:
                errors.append('该手机号已注册')
                print errors
                return render_to_response('reg.html',{'errors':errors})

            # user input verify
            user = tzy_users.objects.create_user(username=username,password=password,email=email,nickname=username)
            if phone is not None:
                user.mobilephone = phone
            user.is_active = True
            user.save()
            auth_user = auth.authenticate(username=username,password=password)
            auth.login(request, auth_user)
            return render_to_response('reg.html',{'user':user})

    print errors
    return render_to_response('reg.html',{'errors':errors})

def regUserInfo(request):
    phone = None
    qq = None
    is_student = None
    errors=[]

    if request.method == 'POST':
        phone = request.POST.get('phone')
        qq = request.POST.get('qq')
        is_student = request.POST.get('is-student')
        
        if request.user.is_authenticated():
            print request.user
            request.user.mobilephone = phone
            request.user.qq = qq
            request.user.is_student = is_student
            request.user.save() 
            return render_to_response('reg.html',{'is_success':True})

    return render_to_response('reg.html')

def loginAction(request):
    errors = []
    user = None
    result = False

    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        print "login-username:"+username
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            result = True
        elif user is None:
            filterResults = tzy_users.objects.filter(mobilephone=username)
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
    return render_to_response('login.html',{"errors":errors})

def checkUser(request):
    req = json.loads(request.body)

    filterResults = []
    if req.has_key('username'):
        username = req['username']
        filterResults = tzy_users.objects.filter(username=username)
    elif req.has_key('phone'):
        phone = req['phone']
        filterResults = tzy_users.objects.filter(mobilephone=phone)
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
    return HttpResponse(json_data,content_type="application/json")