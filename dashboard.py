import streamlit as st
from helpers import load_column

st.title("Sensor Dashboard")

temperatures = load_column("readings.csv", "temperature")
humidity = load_column("readings.csv", "humidity")
co2 = load_column("readings.csv", "co2")

st.metric("Total readings", len(temperatures))

col1, col2, col3 = st.columns(3)
col1.metric("Avg temperature (°C)", round(sum(temperatures) / len(temperatures), 1))
col2.metric("Avg humidity (%)", round(sum(humidity) / len(humidity), 1))
col3.metric("Avg CO2 (ppm)", round(sum(co2) / len(co2), 1))

if max(temperatures) > 21:
    st.warning("Warning: hot!")
else:
    st.success("Temperature is normal")

st.subheader("Temperature")
st.line_chart(temperatures)

st.subheader("Humidity")
st.line_chart(humidity)

st.subheader("CO2")
st.line_chart(co2)