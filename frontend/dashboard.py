import streamlit as st
import requests

st.set_page_config(page_title="Road Weather & Traffic", layout="centered")
st.title("🌦️ Road Weather & Traffic Insight")

city = st.text_input("Enter city name", "Brisbane")

if st.button("Get Insights"):
    weather = requests.get("http://localhost:8000/weather", params={"city": city}).json()
    traffic = requests.get("http://localhost:8000/traffic", params={"city": city}).json()

    st.subheader("☁️ Weather Details")
    st.write(f"Temperature: {weather['main']['temp']}°C")
    st.write(f"Weather: {weather['weather'][0]['description']}")
    st.write(f"Humidity: {weather['main']['humidity']}%")

    st.subheader("🚗 Traffic Details")
    st.write(f"Status: {traffic['status']}")
    st.write(f"Congestion Level: {traffic['congestion_level']}")
    st.write(f"Reported Accidents: {traffic['accidents']}")
