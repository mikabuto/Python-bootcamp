import redis
import logging
import time
import json
from random import randint, choice

r = redis.Redis(host='localhost', port=6379, db=0)

ids = [randint(10**9, 10**10) for _ in range(10)]
print(*ids, sep="\n")

while True:
    message = json.dumps({
        "metadata": {
            "from": choice(ids),
            "to": choice(ids)
        },
        "amount": randint(-5000, 5000)
    })
    print(f"Produced message: {message}")
    r.publish('Cash_Flow', message)
    time.sleep(1)