import csv
import db

count = 0
with open("readings.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        db.add_reading(
            row["time"],
            float(row["temperature"]),
            float(row["humidity"]),
            float(row["co2"]),
        )
        count += 1

print(f"Imported {count} readings")