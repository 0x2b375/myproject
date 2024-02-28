import paho.mqtt.client as mqtt
from django.conf import settings

def on_connect(mqtt_client, userdata, flags, rc, properties):
  if rc == 0:
    print(f"Connected successfully!")
    mqtt_client.subscribe("0aefjk5643/")
  else:
    print('Failed to connect!')    

   

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)

client.connect(
  host = settings.MQTT_SERVER,
  port = settings.MQTT_PORT,
  keepalive = settings.KEEP_ALIVE
)
