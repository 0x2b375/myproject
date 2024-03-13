from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from myproject.mqtt import client as mqtt_client
from .models import Sensor
from .forms import SensorForm
# Create your views here.

def index(request):
  return render(request, 'main/index.html')

def command_center(request):
  return render(request, 'main/command_center.html')

def command_submit(request):
  if request.method == "POST":
    cmd = request.POST.get("your_text")
    mqtt_client.publish('0aefjk5643/', cmd)
    
  return render(request, 'main/command_center.html')

def add_sensor(request):
    if request.method == 'POST':
        form = SensorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SensorForm()
    return render(request, 'main/add_sensor.html', {'form': form})
