import paho.mqtt.client as mqtt
import json
def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    # Feed data to neural network
    # Example: model.predict(data["sensors"], data["camera_features"])
client = mqtt.Client()
client.on_message = on_message
client.username_pw_set(ACCESS_TOKEN)
client.connect(BROKER, 1883)
client.subscribe("v1/devices/me/telemetry")
client.loop_forever()