import requests
import json

API_KEY = "c32ff595107660e367792b7520a4452e"  
lat = 28.3949
lon = 84.1240

def get_weather_data():
    API_URL = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={API_KEY}"

    response = requests.get(API_URL)
    
    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print("Error retrieving weather data.")
        return None

weather_data = get_weather_data()

if weather_data:
    
    print(weather_data)
else:
    print("No weather data available.")
