import csv
import matplotlib.pyplot as plt

temperatures = []
humidity = []

with open("readings.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        temperatures.append(float(row["temperature"]))
        humidity.append(float(row["humidity"]))

plt.figure(figsize=(8, 6))

plt.subplot(2, 1, 1)
plt.plot(temperatures, color="red")
plt.title("Temperature")
plt.ylabel("°C")

plt.subplot(2, 1, 2)
plt.plot(humidity, color="blue")
plt.title("Humidity")
plt.ylabel("%")
plt.xlabel("Reading number")

plt.tight_layout()
plt.savefig("chart.png")
plt.show()