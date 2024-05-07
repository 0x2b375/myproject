from django.shortcuts import render, redirect, get_object_or_404
from myproject.mqtt import client as mqtt_client
from .models import Sensor
from .forms import SensorForm
from django.views.decorators.csrf import csrf_exempt
from awscrt import mqtt
from awsiot import mqtt_connection_builder
import json
import threading
import time
from django.conf import settings

# received_count = 0


# def on_message_received(topic, payload, **kwargs):
#     global received_count
#     received_count += 1
#     print(f"Received message from topic '{topic}': {payload}")
def on_message_received(topic, payload, **kwargs):
    print(f"Received message from topic '{topic}': {payload}")

def mqtt_listener():
    topic = 'test/testing'

    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=settings.AWS_IOT_ENDPOINT,
        port=settings.AWS_IOT_PORT,
        cert_filepath=settings.AWS_IOT_CERT,
        pri_key_filepath=settings.AWS_IOT_KEY,
        ca_filepath=settings.AWS_IOT_CA,
        on_message_received=on_message_received,
        client_id=settings.AWS_IOT_CLIENT_ID,
        clean_session=False,
        keep_alive_secs=30)

    connect_future = mqtt_connection.connect()
    connect_future.result()

    subscribe_future, _ = mqtt_connection.subscribe(
        topic=topic,
        qos=mqtt.QoS.AT_LEAST_ONCE,
        callback=on_message_received)
    subscribe_future.result()

    try:
        while True:
            # Keep the thread running indefinitely
            pass
    except KeyboardInterrupt:
        # Gracefully disconnect the MQTT client when the program is terminated
        disconnect_future = mqtt_connection.disconnect()
        disconnect_future.result()

threading.Thread(target=mqtt_listener, daemon=True).start()

@csrf_exempt
def command_submit(request):
    if request.method == 'POST':
        # Parse request data, e.g., message, topic, etc.
        message = request.POST.get('your_text')
        topic = 'test/testing'

        mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=settings.AWS_IOT_ENDPOINT,
            port=settings.AWS_IOT_PORT,
            cert_filepath=settings.AWS_IOT_CERT,
            pri_key_filepath=settings.AWS_IOT_KEY,
            ca_filepath=settings.AWS_IOT_CA,
            on_message_received=on_message_received,
            client_id=settings.AWS_IOT_CLIENT_ID,
            clean_session=False,
            keep_alive_secs=30)
        connect_future = mqtt_connection.connect()
        connect_future.result()
  
        subscribe_future, _ = mqtt_connection.subscribe(
            topic=topic,
            qos=mqtt.QoS.AT_LEAST_ONCE,
            callback=on_message_received)
        subscribe_future.result()
  
        mqtt_connection.publish(
            topic=topic,
            payload=json.dumps(message),
            qos=mqtt.QoS.AT_LEAST_ONCE)
   
        return render(request, 'main/command_center.html')
    return render(request, 'main/command_center.html')
      
def index(request):
  return render(request, 'main/index.html')

def command_center(request):
  return render(request, 'main/command_center.html')


# def command_submit(request):
#   if request.method == "POST":
#     cmd = request.POST.get("your_text")
#     mqtt_client.publish('0aefjk5643/', cmd)
    
#   return render(request, 'main/command_center.html')

def add_sensor(request):
    if request.method == 'POST':
        form = SensorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sensor_list')
    else:
        form = SensorForm()
    return render(request, 'main/add_sensor.html', {'form': form})

def sensor_list(request):
  sensors = Sensor.objects.all()
  context = {
      'sensors': sensors
  }
  
  return render(request, 'main/sensor_list.html', context)

def edit_sensor(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    # Add logic to handle editing the sensor data
    return render(request, 'edit_sensor.html', {'sensor': sensor})

def delete_sensor(request, sensor_id):
    if request.method == 'POST':    
      sensor = get_object_or_404(Sensor, pk=sensor_id)
      sensor.delete()
      return redirect('sensor_list')
 