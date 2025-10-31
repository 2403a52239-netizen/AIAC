import requests
import json

def get_weather(city_name):
    api_key = '0ccf020f12840b0b776fe94c31d5c407'  # Replace with your actual API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()
    print(json.dumps(weather_data, indent=4))

# Example usage:
city = input("Enter city name: ")
get_weather(city)