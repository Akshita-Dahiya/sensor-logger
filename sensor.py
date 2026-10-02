import random
import time
import csv
import os
from datetime import datetime

current_temp = 19.0

def read_temperature():
    global current_temp
    current_temp += random.uniform(-0.5, 0.5)
    return round(current_temp, 1)
def read_humidity():
    return round(random.uniform(40.0, 80.0) ,1)   
def read_co2():
    return round(random.uniform(400.0, 1200.0) ,1) 

file_exists = os.path.exists("readings.csv")

with open("readings.csv", "a", newline = "") as file:
    writer = csv.writer(file)    
    if not file_exists:
        writer.writerow(["time", "temperature", "humidity", "co2"])
    

    for i in range (10):
        now = datetime.now().strftime("%H:%M:%S")
        temp = read_temperature()
        hum = read_humidity()
        co2 = read_co2()
        writer.writerow([now, temp, hum, co2])
        print(f"{now} | {temp} °C | {hum} % | {co2} ppm")
        time.sleep(0.5)
