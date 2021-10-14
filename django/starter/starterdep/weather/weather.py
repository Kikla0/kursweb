import requests as req
import datetime
from datetime import timedelta

class Weather:
    def get_input(self, key, city, date):
        if city == '':
            city = 'Warszawa'
        
        if date == '' or date =='no':
            date = datetime.date.today() + timedelta(days=1)

        return self.call_api(key, city, date)

    def call_api(self, key, city, date):
        city_ = city.replace(' ', '_')
        r = req.get(f'https://api.weatherapi.com/v1/history.json?key={key}&q={city_}&dt={date}')
        r = r.json()
        city = r['location']['name']
        rain = r['forecast']['forecastday'][0]['day']['totalprecip_mm']
        if rain == 0:
            rain = "Nie"
        else:
            rain = "Tak"
        weather = {'rain': rain,
                    'avg': r['forecast']['forecastday'][0]['day']['avgtemp_c'],
                    'min': r['forecast']['forecastday'][0]['day']['mintemp_c'],
                    'max': r['forecast']['forecastday'][0]['day']['maxtemp_c'],
                    'hum': r['forecast']['forecastday'][0]['day']['avghumidity'],
                    'wind': r['forecast']['forecastday'][0]['day']['maxwind_kph']}
        return self.return_weather(city, date, weather)

    def return_weather(self, city, date, weather):
        output = {
            'city': city,
            'date': date,
            'rain': weather["rain"],
            'avg': weather["avg"],
            'min': weather["min"],
            'max': weather["max"],
            'hum': weather["hum"],
            'wind': weather["wind"]
        }
        return output                

weather = Weather()
