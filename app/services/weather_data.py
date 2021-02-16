from expiringdict import ExpiringDict
import requests


def get_weather_api_data():
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q={London}&appid={735996eca8cef83770eb27e49446bc6c}')

    weather_list = []

    return response


def filter_response(data):
    filtered_response = {'City_name': 'data',
                         'City_temp': 'data', 'City_condition': 'data'}

    return filtered_response


def cache_response(data):
    pass
