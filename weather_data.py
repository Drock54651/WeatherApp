from settings import *
import json
import requests

def get_weather(latitude, longitude, units, period):
    full_url = f'{BASE_URL}lat={latitude}&lon={longitude}&appid={API_KEY}&units={units}'
    response = requests.get(full_url)

    current_data = {}
    forecast_data = {}

    if response.status_code == 200: #! if not 200, then means some error code happened
        data = response.json()#! json is basically just a dictionary
        for key, value in data.items(): 
            if key == 'list':
                for index, data_entry in enumerate(value): #! data entry is a list with dictionaires within dictionaries
                    
                    if index == 0:
                        current_data['temp'] = int(round(data_entry['main']['temp'],0))
                        current_data['feels_like'] = int(round(data_entry['main']['feels_like'],0))
                        current_data['weather'] = data_entry['weather'][0]['main']
                        today = data_entry['dt_txt'].split(' ')[0] #! dt_txt looks like 'dt_txt': '2023-09-30 09:00:00', grabs todays date
                        
                    else: #! grabs forecast data for next 5 days
                        if data_entry['dt_txt'].split(' ')[0] != today: #! when next day occurs
                            start_index = index + 4 #! +4 for noon the next day 
                            break

        for index in range(start_index , len(data['list']), 8): #! step size of 8
            forecast_entry = data['list'][index]
            date = forecast_entry['dt_txt'].split(' ')[0]
            forecast_data[date] = {'temp': int(round(forecast_entry['main']['temp'],0)), 
                                   'feels_like': int(round(forecast_entry['main']['feels_like'],0)), 
                                   'weather': forecast_entry['weather'][0]['main']}

    if period == 'today':
        return current_data
    
    else:
        return forecast_data