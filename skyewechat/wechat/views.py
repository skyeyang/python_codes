#coding:utf-8
import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world! - Django")

TOKEN = "weixin"
@csrf_exempt  
def index(request):  
    if request.method == 'GET':  
        response = HttpResponse(checkSignature(request),content_type="text/plain")  
        return response  
    elif request.method == 'POST':  
        response = HttpResponse("POST METHOD")  
        return response  
    else:  
        return None  
  
def checkSignature(request):  
    global TOKEN  
    signature = request.GET.get("signature", None)  
    timestamp = request.GET.get("timestamp", None)  
    nonce = request.GET.get("nonce", None)  
    echoStr = request.GET.get("echostr",None)  
  
    token = TOKEN  
    tmpList = [token,timestamp,nonce]  
    tmpList.sort()  
    tmpstr = "%s%s%s" % tuple(tmpList)  
    tmpstr = hashlib.sha1(tmpstr).hexdigest()  
    if tmpstr == signature:  
        return echoStr  
    else:  
        return None
