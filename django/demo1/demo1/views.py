from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def index(request):
    # return HttpResponse(datetime.datetime.now())
    return render(request, "index.html", dict(d=datetime.datetime.now()))

