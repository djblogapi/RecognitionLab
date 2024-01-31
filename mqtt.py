import random
import time

import paho.mqtt.client as mqtt

# Set the MQTT broker's address and port
BROCKER_ADDRESS = "localhost"
BROCKER_PORT = 1883

# Set the topic to subscribe to
TOPIC = "face_recognition"

# Callback when a message is received
# def on_message(client, userdata, msg):/
#     print(f"Received message: {msg.payload.decode()}")


# Create an MQTT client
client = mqtt.Client()

# Set the callback for message reception
# client.on_message = on_message/

# Connect to the MQTT broker
client.connect(BROCKER_ADDRESS, BROCKER_PORT, 60)

# Subscribe to the topic
# client.subscribe(TOPIC)
#
# # Loop to continuously listen for messages
# client.loop_forever()


# def on_publish(client, userdata, result):
#     print("Device 1 : Data published.")
#     # raise Exception("Device 1 : Data published.")
#     print(client, userdata, result)

client = mqtt.Client()
client.connect("localhost", 1883, 60)
# client.on_publish = on_publish
# def publish_temperature():
#     client = mqtt.Client()
#     client.connect("localhost", 1883, 60)
#     client.on_publish = on_publish
#
#     cnt = 1
#     while True:
#         temperature = round(random.uniform(20, 30), 2)
#         cnt += 1
#         client.publish("face_recognition", f"{cnt}:{temperature} °C")
#
#         time.sleep(5)
#         print(temperature)
