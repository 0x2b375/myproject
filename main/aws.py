import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
from django.conf import settings

def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload.decode("utf-8"))
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

ENDPOINT = "a17h1l6mwhc3vh-ats.iot.ap-northeast-1.amazonaws.com"
CLIENT_ID = "891377292691"
PATH_TO_CERT = "C:/Users/Acer Nitro 5/Downloads/IoT Cloud computing/django-lab/myproject/main/certificates/a5ed70146186412b5d1a1cfbfd10aeea3fd0b96b0d85d0548648791d5667763a-certificate.pem.crt"
PATH_TO_KEY = "C:/Users/Acer Nitro 5/Downloads/IoT Cloud computing/django-lab/myproject/main/certificates/a5ed70146186412b5d1a1cfbfd10aeea3fd0b96b0d85d0548648791d5667763a-private.pem.key"
PATH_TO_ROOT = "C:/Users/Acer Nitro 5/Downloads/IoT Cloud computing/django-lab/myproject/main/certificates/AmazonRootCA1.pem"
MESSAGE = "Hello from Django"
TOPIC = "test/testing"
RANGE = 5

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

myAWSIoTMQTTClient.connect()
print("Successfully connected")
myAWSIoTMQTTClient.subscribe(TOPIC, 1, customCallback)
print(f"Subscribed to topic: {TOPIC}")

print('Begin Publish')
for i in range(RANGE):
    data = "{} [{}]".format(MESSAGE, i+1)
    message = {"message": data}
    myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1)
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
    t.sleep(0.1)

print('Publish End')

  
while True:
    t.sleep(1)
