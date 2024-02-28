from django.shortcuts import render
import json
from django.http import JsonResponse
from myproject.mqtt import client as mqtt_client
# Create your views here.



def index(request):
  return render(request, 'main/index.html')

def publish_message(request):
  request_data = json.loads(request.body)
  rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
  return JsonResponse({'code': rc})