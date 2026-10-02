Sensor Logger
A beginner-friendly Python project that simulates an IoT sensor node.
It generates fake temperature, humidity and CO2 readings, saves them to a CSV file, analyses the data (minimum, maximum, average and a high-temperature warning), and plots the results as a chart. 
It is built in plain Python with no hardware, as a foundation for later IoT projects where the simulated sensor can be swapped for a real one.
How it works
Sensor (sensor.py): generates a reading every half second and appends it to readings.csv. The header row is written only once, even across multiple runs.
Storage (readings.csv): one row per reading with the columns time, temperature, humidity and co2.
Analysis (analyse.py): reads the CSV and prints the minimum, maximum and average for temperature and humidity, plus a warning if the maximum temperature is above 21 °C.
Visualisation (plot.py): draws temperature and humidity on separate charts and saves them as chart.png.
How to run
Requires Python 3 and matplotlib:
pip install matplotlib
Then run the scripts in this order:
python sensor.py     # generate and log readings (run it a few times)
python analyse.py    # print summary statistics
python plot.py       # show the chart and save chart.png
