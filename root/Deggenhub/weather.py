import requests
from config.settings.base import env

import math
import datetime

def get_weather():

        api_key = env("WEATHER_API_KEY")
        lat = '48.8333535'
        lon = '12.96205'
        base_url = "http://api.openweathermap.org/data/2.5/weather?"        
        complete_url = f"{base_url}lat={lat}&lon={lon}&appid={api_key}&units=metric"
        
        response = requests.get(complete_url)
        try:
            if response.status_code == 200:


                weather_data = response.json()   
                temperature = math.floor(weather_data['main']['temp'])
                temp_min = math.floor(weather_data['main']['temp_min'])
                temp_max = math.floor(weather_data['main']['temp_max'])
                weather_description = weather_data['weather'][0]['description']
                icon = weather_data['weather'][0]['icon']
                date = datetime.datetime.now().strftime("%a, %d %b")
                wind_speed = math.floor(weather_data['wind']['speed'] * 3.6)
                humidity = weather_data['main']['humidity']
                
                context = {
                'temperature': temperature,
                'weather_description': weather_description,
                'temp_min': temp_min,
                'temp_max': temp_max,
                'icon': icon,
                'date': date,
                'wind_speed': wind_speed,
                'humidity': humidity
                }

                
        except:
                context = {
                'temperature': 'N/A',
                'weather_description': 'N/A',
                'temp_min': 'N/A',
                'temp_max': 'N/A',
                'icon': 'N/A',
                'date': 'N/A',
                'wind_speed': 'N/A',
                'humidity': 'N/A'
                }
        return context

get_weather()
