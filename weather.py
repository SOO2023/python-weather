import os
import requests
from dotenv import load_dotenv
from pprint import pprint
import random


load_dotenv()

def get_city_weather(city="Lagos"):
    
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data_json = requests.get(request_url).json()
    
    return weather_data_json


if __name__ == '__main__':

    print('\nCurrent Weather Getter!🌦️ ⛅ ☔')
    degree_sign = u'\N{DEGREE SIGN}'
    
    city = input("\nEnter a city🏙️ 🌆: \n")
    
    if not bool(city.strip()):
        nig_cities = ['Lagos', 'Abuja', 'Ogun', 'Kano', 'Kaduna', 'Gombe', 'Kwara', 'Oyo', 'Edo', 'Zamfara', 'Delta', 'Enugu']
        
        city = random.choice(nig_cities)
        
    weather_data = get_city_weather(city)
    
    if weather_data['cod'] == '404':
        print("\nOops! The weather of the city entered could not be found.\n")
    
    else:
        print(f"\nThe current weather in {weather_data['name']}, {weather_data['sys']['country']}.")
        print(f"\nThe temperature is {weather_data['main']['temp']}{degree_sign}C🌡️ ☁️")
        print(f"\nThe weather in {weather_data['name']} feel like: {weather_data['weather'][0]['description']}⛅ 🌩️ 🌦️ 🌧️\n")
            
    