
from django.http import HttpResponse
from django.db import transaction, connections
from . import models
import datetime


def index(request):
    connec = connections['default']
    connec.set_autocommit(False)
    models.Question.objects.create(question_text='xxxx111', pub_date=datetime.datetime.now())
    
    models.Question.objects.create(question_text='xxxx222', pub_date=datetime.datetime.now())
    # connec.commit()
    x = 0
    y = 10 / x
    
    return HttpResponse("Hello, world. You're at the polls index.%s" % y)


def update(request):
    connec = connections['default']
    connec.set_autocommit(False)
    sql = "update polls_question set pub_date=now() where id=47"
    with connec.cursor() as cur:
        cur.execute(sql)
        connec.commit()
    return HttpResponse(sql)


def slow(request):
    
    connec = connections['default']
    #connec.set_autocommit(False)
    sql = "select sleep(3),question_text,pub_date from polls_question where id=1";
    with connec.cursor() as cur:
        # cur.execute("set long_query_time = 1")
        cur.execute(sql)
        # cur.fetchall()
    
    return HttpResponse('slow sql is:%s' % sql)


def index2(request):
    return HttpResponse('heelellllx:%s' % connections['default'].get_autocommit())
