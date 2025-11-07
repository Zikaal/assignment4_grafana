#!/usr/bin/env python3
import requests
import time
from prometheus_client import start_http_server, Gauge

# === Настройки ===
API_KEY = "f8f916e3c6e2b6d10914be4a0b9fcb24"  # ← ВСТАВЬТЕ СЮДА
CITY = "Moscow,RU"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# === Метрики (10 штук) ===
g_temp = Gauge('weather_temperature_celsius', 'Current temperature in °C')
g_feels_like = Gauge('weather_feels_like_celsius', 'Feels like temperature in °C')
g_humidity = Gauge('weather_humidity_percent', 'Humidity in %')
g_pressure = Gauge('weather_pressure_hpa', 'Atmospheric pressure in hPa')
g_wind_speed = Gauge('weather_wind_speed_mps', 'Wind speed in m/s')
g_wind_deg = Gauge('weather_wind_direction_deg', 'Wind direction in degrees')
g_clouds = Gauge('weather_cloudiness_percent', 'Cloudiness in %')
g_visibility = Gauge('weather_visibility_meters', 'Visibility in meters')
g_sunrise = Gauge('weather_sunrise_unix', 'Sunrise time (Unix)')
g_sunset = Gauge('weather_sunset_unix', 'Sunset time (Unix)')

def fetch_weather():
    try:
        r = requests.get(URL, timeout=10)
        r.raise_for_status()
        data = r.json()

        g_temp.set(data['main']['temp'])
        g_feels_like.set(data['main']['feels_like'])
        g_humidity.set(data['main']['humidity'])
        g_pressure.set(data['main']['pressure'])
        g_wind_speed.set(data['wind']['speed'])
        g_wind_deg.set(data['wind']['deg'])
        g_clouds.set(data['clouds']['all'])
        g_visibility.set(data.get('visibility', 0))
        g_sunrise.set(data['sys']['sunrise'])
        g_sunset.set(data['sys']['sunset'])

        print(f"[OK] Updated at {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == '__main__':
    start_http_server(8000)
    print("Custom Exporter запущен на http://localhost:8000/metrics")
    while True:
        fetch_weather()
        time.sleep(20)
