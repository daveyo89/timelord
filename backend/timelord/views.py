import datetime
import json

from bson import json_util
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend import db


@api_view()
def home(request):
    data = db['test'].find({})
    d = [e for e in data]
    details_json_string = json.dumps(d, default=json_util.default)

    return Response(json.loads(details_json_string))


def home_add(request):
    _id = db['test'].insert_one({'hello': datetime.datetime.now()})
    print(_id)
    return HttpResponse(f'Sikerült: {_id.inserted_id}')
