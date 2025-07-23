import cv2
import paho.mqtt.client as mqtt
import json
cap = cv2.VideoCapture(0)
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(BROKER, 1883)
while True:
    ret, frame = cap.read()
    intensity = frame.mean()  # Example feature
    data = {"camera_intensity": intensity}
    client.publish("v1/devices/me/telemetry", json.dumps(data))
    time.sleep(0.1)