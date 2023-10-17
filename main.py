from flask import Flask, render_template, request
from weather import get_city_weather
import random


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def city_weather():
    
    city = request.args.get('city')
    
    if not bool(city.strip()):
        nig_cities = ['Lagos', 'Abuja', 'Ogun', 'Kano', 'Kaduna', 'Gombe', 'Kwara', 'Oyo', 'Edo', 'Zamfara', 'Delta', 'Enugu']
        
        city = random.choice(nig_cities)
        
    weather_data = get_city_weather(city)
    
    if weather_data['cod'] == '404':
        return render_template('error.html')

    return render_template(
        'weather.html',
        city=weather_data["name"],
        country=weather_data['sys']['country'],
        temp=weather_data['main']['temp'],
        feels_like=weather_data['weather'][0]['description']
        )       


if __name__ == "__main__":
    app.run(debug=True)
