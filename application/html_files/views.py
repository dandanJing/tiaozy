#encoding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from application.ssl_users.models import tzy_users
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return render_to_response('index.html',{'login_user':request.user})
    else:
        auth.logout(request)
        return render_to_response('index.html')

def publish(request):
    if request.user.is_authenticated():
        return render_to_response('publish.html')
    else:
        return render_to_response("login.html")

def pub_1(request):
    typeIndex = 1
    username = None
    mobile = None
    if not request.user.is_authenticated():
        return render_to_response("login.html")
    try:
        if request.method == "GET":
            typeIndex = request.GET.get('type')
        username =  request.user.username
        mobile = request.user.Mobilephone
    except Exception as e:
        logger.debug('pub_1: %s' % e)
    print 'type: %s'%(typeIndex)
    return render_to_response('pub_1.html',{'typeIndex':typeIndex,'username':username,'mobile':mobile})

def askItem(request):
    return render_to_response('ask_item.html')