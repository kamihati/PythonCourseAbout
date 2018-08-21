# coding=utf8
import json


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    res = json.dumps(dict(a=1, b=3, c=['我', '来', '也']))
    return [b'<b>%s</b>' % res]