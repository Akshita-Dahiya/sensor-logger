import csv
import matplotlib.pyplot as plt

def load_column(filename, column):
    values = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            values.append(float(row[column]))
    return values

temperatures = load_column("readings.csv", "temperature")
humidity = load_column("readings.csv", "humidity")

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