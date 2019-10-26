import datetime
import pandas as pd
import os
import json
import matplotlib.pyplot as plt

current_date_time = None

def get_latest_weather_data():
    global current_date_time
    filename = 'darksky_data/raw_data/weather.json'
    with open(filename) as f:
        data = json.load(f)
        
    df = pd.DataFrame(data['hourly']['data'])
    
    # Convert time into a proper datetime object
    df['time'] = pd.to_datetime(df['time'], unit='s')
    
    # Set the current date time of the data in the global variable. This will be accessed later.
    current_date_time = datetime.datetime.fromtimestamp(data['currently']['time']).strftime('%Y_%m_%d_%H_%M')
    return df

df = get_latest_weather_data()

def write_csv_file(dataframe):
    folder_name = 'darksky_data/output_data/{0}'.format(current_date_time)
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)
        
    filename = os.path.join(folder_name, 'output.csv')
    dataframe.to_csv(filename, index=False)
    
write_csv_file(df)

def calculate_temperature_stats(dataframe):
    temperature_data = {'stat': 'temperature'}
    temperature_data['max'] = dataframe['temperature'].max()
    temperature_data['min'] = dataframe['temperature'].min()
    temperature_data['average'] = dataframe['temperature'].mean()
    return temperature_data

stats = []
stats.append(calculate_temperature_stats(df))

def calculate_windspeed_stats(dataframe):
    temperature_data = {'stat': 'windspeed'}
    temperature_data['max'] = dataframe['windSpeed'].max()
    temperature_data['min'] = dataframe['windSpeed'].min()
    temperature_data['average'] = dataframe['windSpeed'].mean()
    return temperature_data

stats.append(calculate_windspeed_stats(df))


folder_name = 'darksky_data/output_data/{0}'.format(current_date_time)
filename = os.path.join(folder_name, 'output.csv')
pd.DataFrame(stats).to_csv(filename, index=False)

def plot_temperature(dataframe):
    folder_name = 'darksky_data/output_data/{0}'.format(current_date_time)
    filename = os.path.join(folder_name, 'temperature.png')
    df.plot.line(x='time', y='temperature')
    plt.savefig(filename)
    
plot_temperature(df)


def plot_windspeed(dataframe):
    folder_name = 'darksky_data/output_data/{0}'.format(current_date_time)
    filename = os.path.join(folder_name, 'windspeed.png.png')
    df.plot.line(x='time', y='windSpeed')
    plt.savefig(filename)
    
plot_windspeed(df)



