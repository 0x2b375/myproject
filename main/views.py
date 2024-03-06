from django.shortcuts import render
import json
from django.http import JsonResponse
from myproject.mqtt import client as mqtt_client
# Create your views here.

def index(request):
  mqtt_client.publish('0aefjk5643/', 'HELLO FROM DJANGO')
  return render(request, 'main/index.html')

def command_center(request):
  return render(request, 'main/command_center.html')