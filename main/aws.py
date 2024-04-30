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

MESSAGE = "Hello from Django"
TOPIC = "test/testing"
RANGE = 5

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(settings.CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(settings.ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(settings.PATH_TO_ROOT, settings.PATH_TO_KEY, settings.PATH_TO_CERT)

myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe(TOPIC, 1, customCallback)

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
