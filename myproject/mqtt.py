import paho.mqtt.client as mqtt
from django.conf import settings

def on_connect(mqtt_client, userdata, flags, rc, properties):
  if rc == 0:
    print(f"Connected successfully!")
    # mqtt_client.subscribe("0aefjk5643/")
  else:
    print('Failed to connect!')    

  
def on_message(client, userdata, msg):
    print(f'Received message on topic: {msg.topic} with payload: {str(msg.payload)}')
    

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)

client.connect(
  host = settings.MQTT_SERVER,
  port = settings.MQTT_PORT,
  keepalive = settings.MQTT_KEEPALIVE
)
