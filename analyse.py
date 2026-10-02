import csv

temperatures = []
humidity = []

with open("readings.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        temperatures.append(float(row["temperature"]))
        humidity.append(float(row["humidity"]))

print("Total readings:", len(temperatures))

print("--- Temperature ---")
print("Minimum:", min(temperatures))
print("Maximum:", max(temperatures))
print("Average:", round(sum(temperatures) / len(temperatures), 1))

print("--- Humidity ---")
print("Minimum:", min(humidity))
print("Maximum:", max(humidity))
print("Average:", round(sum(humidity) / len(humidity), 1))

if max(temperatures) > 21:
    print("Warning: hot!")
else :
    print("Temperature is normal")    