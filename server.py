from fastapi import FastAPI
from pydantic import BaseModel
import db

app = FastAPI()


class Reading(BaseModel):
    time: str
    temperature: float
    humidity: float
    co2: float


@app.post("/readings")
def add_reading(reading: Reading):
    db.add_reading(reading.time, reading.temperature, reading.humidity, reading.co2)
    return {"status": "saved"}


@app.get("/readings")
def get_readings():
    count = db.count_readings()
    if count == 0:
        return {"count": 0}
    latest = db.latest_readings(1)[0]
    return {"count": count, "latest_temperature": latest["temperature"]}


@app.get("/readings/max")
def get_max_temperature():
    return {"max_temperature": db.max_temperature()}


@app.get("/readings/latest")
def get_latest(limit: int = 5):
    return db.latest_readings(limit)

@app.get("/readings/min")
def get_min_temperature():
    return {"min_temperature": db.min_temperature()}