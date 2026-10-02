import streamlit as st
import db

st.title("Sensor Dashboard")

temperatures = db.get_column("temperature")
humidity = db.get_column("humidity")
co2 = db.get_column("co2")

if not temperatures:
    st.info("No readings yet. Start the server and run send_readings.py.")
    st.stop()
    
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