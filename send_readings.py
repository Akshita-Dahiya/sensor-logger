import random
import time
from datetime import datetime
import requests

URL = "http://127.0.0.1:8000/readings"

temp = 19.0

for i in range(10):
    temp += random.uniform(-0.5, 0.5)
    reading = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "temperature": round(temp, 1),
        "humidity": round(random.uniform(40.0, 80.0), 1),
        "co2": round(random.uniform(400.0, 1200.0), 1),
    }
    response = requests.post(URL, json=reading)
    print(response.status_code, reading)
    time.sleep(1)