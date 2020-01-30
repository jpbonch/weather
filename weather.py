from flask import Flask, render_template
from pyowm import OWM
from datetime import datetime


app = Flask(__name__)

API_key = 'fb58b1ad50f20581ddeb9b35254bf1b4'
owm = OWM(API_key)

@app.route('/')
def index():

    place = 'London'
    obs = owm.weather_at_place(place)
    w = obs.get_weather()

    time = datetime.now().strftime("%A, %H:%M")

    icon = w.get_weather_icon_url()

    temp = str(int(w.get_temperature(unit='celsius')['temp'])) + '°C'
    humid = 'humidity: ' + str(w.get_humidity()) + '%'
    wind = 'wind speed: ' + str(float(w.get_wind()['speed']) * 3.6) + 'km/h'
    status = w.get_detailed_status()

    weather_data = []
    weather_data.extend([place, time, temp, humid, wind, status, icon])

    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
	app.run()
