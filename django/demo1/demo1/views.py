from django.shortcuts import render
from django.http import HttpResponse
import datetime
import json
from django.views.decorators.csrf import csrf_exempt

from django.http import QueryDict

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import UploadFileForm
from django.conf import settings
import os
from django.urls import reverse
from polls.models import PollMan


@csrf_exempt
def index(request):
    
    if request.method == "POST":
        dd = dict(aa=request.POST.get('xx', 'xxxxx'))
        return HttpResponse(json.dumps(dd), content_type='application/json')
    # return HttpResponse(datetime.datetime.now())
    return render(request, "index.html", dict(d=datetime.datetime.now()))


@csrf_exempt
def get_json(request):
    result = {"a": 1, "b": 2, "c": "少干城"}
    return HttpResponse(json.dumps(result))


def write(request):
    response = HttpResponse()
    response.set_signed_cookie("username", "12345", salt="234", path="/", domain='127.0.0.1')
    response.write("username=" + request.get_signed_cookie("username", salt="234"))
    return response


def read(request):
    response = HttpResponse()
    # response.delete_cookie("username", path="/", domain='127.0.0.1')
    response.write("username=" + request.get_signed_cookie("username", salt="234"))
    return response


def upload_m(request):
    response = HttpResponse()
    return response


def handle_uploaded_file(f):
    file_path = os.path.join(settings.BASE_DIR, 'upload/one.jpg')
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == 'POST':
        
        # 直接保存文件
        # handle_uploaded_file(request.FILES['file'])
        
        # 使用model上传
        PollMan()
        
        return HttpResponseRedirect(reverse("upload_success"))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def upload_success(request):
    return HttpResponse("success upload")
