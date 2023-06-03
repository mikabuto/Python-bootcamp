import redis
import time
import sys
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

bad_guys = []
if len(sys.argv) > 2 and sys.argv[1] == "-e":
    bad_guys = list(map(int, sys.argv[2].split(',')))

consumer = r.pubsub()
consumer.subscribe("Cash_Flow")

# waiting data: 1
while True:
    message = consumer.get_message()
    if message and message.get("data", 0):
        break
    time.sleep(0.01)

while True:
    message = consumer.get_message()
    if message:
        payload = json.loads(message.get("data", 0))
        if payload['amount'] > 0 and payload['metadata']['to'] in bad_guys:
            payload['metadata']['to'], payload['metadata']['from'] = payload['metadata']['from'], payload['metadata']['to']
        print(payload)
    time.sleep(0.1)