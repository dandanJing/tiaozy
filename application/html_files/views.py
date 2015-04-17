#encoding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return render_to_response('index.html',{'login_user':request.user})
    else:
        auth.logout(request)
        return render_to_response('index.html')

def publishItem(request):
    if request.user.is_authenticated():
        return render_to_response('publish.html')
    else:
        return render_to_response("login.html")

def pub_1(request):
    return render_to_response('pub_1.html')