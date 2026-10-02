import csv
import os
from fastapi import FastAPI
from pydantic import BaseModel
from helpers import load_column

app = FastAPI()
FILENAME = "readings.csv"


class Reading(BaseModel):
    time: str
    temperature: float
    humidity: float
    co2: float


@app.post("/readings")
def add_reading(reading: Reading):
    file_exists = os.path.exists(FILENAME)
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["time", "temperature", "humidity", "co2"])
        writer.writerow([reading.time, reading.temperature, reading.humidity, reading.co2])
    return {"status": "saved"}


@app.get("/readings")
def get_readings():
    if not os.path.exists(FILENAME):
        return {"count": 0}
    temperatures = load_column(FILENAME, "temperature")
    if not temperatures:
        return {"count": 0}
    return {"count": len(temperatures), "latest_temperature": temperatures[-1]}