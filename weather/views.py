from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=4eee41a6e73eab2c22c03c41d3359370'
        res = urllib.request.urlopen(url).read()
        json_data = json.loads(res)
        temperature_kelvin = float(json_data['main']['temp'])
        temperature_celsius = temperature_kelvin - 273.15  # Convert Kelvin to Celsius
        data = {
            "city": city,
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(round(temperature_celsius, 2)) + '°C',  # Round temperature to 2 decimal places
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        data = {}

    return render(request, 'index.html', data)
