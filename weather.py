import os
from flask import Flask, render_template, request
from pyowm import OWM
from datetime import datetime

app = Flask(__name__)

owm_API_key = os.getenv('OWM_API_KEY')
owm = OWM(owm_API_key)

def generate_weather(city_name):
                obs = owm.weather_at_place(city_name)
                w = obs.get_weather()

                time = datetime.now().strftime("%A, %H:%M")

                icon = w.get_weather_icon_url()

                temp = str(int(w.get_temperature(unit='celsius')['temp']))
                humid = 'humidity: ' + str(int(w.get_humidity())) + '%'
                wind = 'wind speed: ' + str(int(float(w.get_wind()['speed']) * 3.6)) + 'km/h'
                status = w.get_detailed_status().capitalize()

                weather_data = [city_name, time, temp, humid, wind, status, icon]
                return weather_data


@app.route('/')
def index():
    error = ''
    weather = generate_weather('London')
    city = request.args.get('city', 'London')
    city = city.title()
    try:
        weather = generate_weather(city)
    except:
        error = 'City not found'


    return render_template('index.html', weather_data=weather, error=error)

if __name__ == '__main__':
	app.run()
