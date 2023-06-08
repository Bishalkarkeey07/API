import requests
import json

API_KEY = "c32ff595107660e367792b7520a4452e"  

def get_weather_data(city):
    API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print("Error retrieving weather data.")
        return None
    
city_name = "kathmandu"
weather_info = get_weather_data(city_name)

if weather_info:
    temperature = weather_info["main"]["temp"]
    weather_description = weather_info["weather"][0]["description"]
    humidity = weather_info["main"]["humidity"]
    
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature} K")
    print(f"Description: {weather_description}")
    print(f"Humidity: {humidity}%")
else:
    print(f"Could not retrieve weather data for {city_name}.")

#the output is 
# Weather in kathmandu:
# Temperature: 303.62 K
# Description: scattered clouds
# Humidity: 41%