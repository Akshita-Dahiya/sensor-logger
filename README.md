# Sensor Logger

A beginner-friendly Python project that simulates an IoT sensor node. It generates fake temperature, humidity and CO2 readings, saves them to a CSV file, analyses the data (minimum, maximum, average and a high-temperature warning), and shows the results as charts and a live dashboard. It is built in plain Python with no hardware, as a foundation for later IoT projects where the simulated sensor can be swapped for a real one.

## How it works

The project follows the same pipeline as a real IoT system, just at a small scale:

1. **Sensor** (`sensor.py`): generates readings and appends them to `readings.csv`. The header row is written only once, even across multiple runs.
2. **Storage** (`readings.csv`): one row per reading with the columns `time`, `temperature`, `humidity` and `co2`.
3. **Analysis** (`analyse.py`): prints the minimum, maximum and average for each measurement, plus a warning if the maximum temperature is above 21 °C.
4. **Visualisation** (`plot.py`): draws temperature and humidity on separate charts and saves them as `chart.png`.
5. **Dashboard** (`dashboard.py`): shows the averages, a temperature warning and live charts in the browser using Streamlit.

Shared code for reading CSV columns lives in `helpers.py`.

## How to run

Requires Python 3 and these libraries:

```
pip install matplotlib streamlit
```

Run the scripts in this order:

```
python sensor.py     # generate and log readings (run it a few times)
python analyse.py    # print summary statistics
python plot.py       # show the chart and save chart.png
```

To view the live dashboard:

```
python -m streamlit run dashboard.py
```

Note: `readings.csv` is created by `sensor.py`, so run it first.

## What I practised

- Functions, loops, lists and `if/else`
- Reading and writing CSV files
- Splitting code into reusable functions and modules
- Plotting data with matplotlib
- Building a dashboard with Streamlit
- Using Git and GitHub from the terminal

## Next steps

- Add CO2 to the charts
- Replace the fake sensor with a real ESP32 sensor node
- Send readings through an API instead of a file