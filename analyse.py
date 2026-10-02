from helpers import load_column

def print_summary(name, values):
    print(f"--- {name} ---")
    print("Minimum:", min(values))
    print("Maximum:", max(values))
    print("Average:", round(sum(values) / len(values), 1))

temperatures = load_column("readings.csv", "temperature")
humidity = load_column("readings.csv", "humidity")
co2 = load_column("readings.csv", "co2")

print("Total readings:", len(temperatures))
print_summary("Temperature", temperatures)
print_summary("Humidity", humidity)
print_summary("co2", co2)

if max(temperatures) > 21:
    print("Warning: hot!")
else:
    print("Temperature is normal")