import datetime
import json
import os
import requests

DARKSKY_API_KEY = '545a8baef85086fcd6187cdd59abc37d'
WEATHER_LOCATION_COORDINATES = '40.7128,-74.0060'

# First, check if the data folder is present. If not, create it
data_folder = 'darksky_data/raw_data'
if not os.path.isdir(data_folder):
    os.makedirs(data_folder)
    
# Generate the URL
url = 'https://api.darksky.net/forecast/{0}/{1}'.format(DARKSKY_API_KEY, WEATHER_LOCATION_COORDINATES)
response = requests.get(url)

weather_data = response.json()
current_datetime = datetime.datetime.fromtimestamp(weather_data['currently']['time']).strftime('%Y_%m_%d_%H_%M')
filename = os.path.join(data_folder, 'weather_{0}.json'.format(current_datetime))
with open(filename, 'w+') as f:
    f.write(json.dumps(weather_data))
    
latest_filename = os.path.join(data_folder, 'weather.json')
with open(latest_filename, 'w+') as f:
    f.write(json.dumps(weather_data))
