from fastapi import FastAPI, Query
import requests

app = FastAPI()

OPENWEATHER_API_KEY = "YOUR_API_KEY"

@app.get("/weather")
def get_weather(city: str = Query(...)):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    res = requests.get(url)
    return res.json()

@app.get("/traffic")
def get_traffic(city: str = Query(...)):
    # Placeholder for real traffic API
    return {
        "city": city,
        "status": "Moderate Traffic",
        "accidents": 2,
        "congestion_level": "Medium"
    }
