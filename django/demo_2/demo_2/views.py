from django.shortcuts import render
from django.http import HttpResponse
import datetime
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return HttpResponse(datetime.datetime.now())
    # return render(request, "index.html", dict(d=datetime.datetime.now()))


@csrf_exempt
def get_json(request):
    result = {"a": 1, "b": 2, "c": "少干城"}
    return HttpResponse(json.dumps(result))


@csrf_exempt
def post_json(request):
    return HttpResponse(json.dumps(request.POST))
