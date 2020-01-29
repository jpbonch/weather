from flask import Flask, render_template
from pyowm import OWM


app = Flask(__name__)

API_key = 'fb58b1ad50f20581ddeb9b35254bf1b4'
owm = OWM(API_key)

@app.route('/')
def index():

    obs = owm.weather_at_place('London')
    w = obs.get_weather()

    temp = str(w.get_temperature(unit='celsius')['temp']) + '°C'
    humid = str(w.get_humidity()) + '%'
    wind = str(float(w.get_wind()['speed']) * 3.6) + 'km/h'
    status = w.get_detailed_status()

    weather_data = []
    weather_data.extend([temp, humid, wind, status])

    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
	app.run()
