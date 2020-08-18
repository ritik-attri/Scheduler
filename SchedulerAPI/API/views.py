from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import TaskSerializer,Tasks
from datetime import datetime
import requests
from dateutil.parser import parse
from rest_framework.response import Response
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        print(request.data['Date_Time'],request.data['URL'])
        date = parse(request.data['Date_Time'])
        Tasks.objects.create(Date_Time=date, URL=request.data['URL'])
        return Response({"Message":"Task Added"})

def checker():
    print("Scheduler running every 1 min")
    now=datetime.now()
    for object in Tasks.objects.all():
        if datetime.date(object.Date_Time)<=datetime.date(now):
            print("inside first loop",datetime.time(object.Date_Time),datetime.time(now))
            if datetime.time(object.Date_Time)<datetime.time(now):
                requests.get(url=object.URL)
                print("Request Sent!")
        else:
            print("Nothing to do!")


def server_check(request):
    return JsonResponse({
        "status":"OK"
    })
