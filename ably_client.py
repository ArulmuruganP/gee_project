# ably_client.py
from ably import AblyRealtime
import json

client = AblyRealtime('your-api-key')  # Replace with your actual key
channel = client.channels.get('traffic-updates')

def subscribe_traffic(callback):
    def on_message(msg):
        data = json.loads(msg.data)
        callback(data)
    channel.subscribe(on_message)
