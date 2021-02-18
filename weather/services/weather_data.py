from flask import Flask
import requests
import json

from weather.models import City


def get_weather_api_data(city_name):
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=735996eca8cef83770eb27e49446bc6c')
    data = json.loads(response._content)

    return data


def selected_response(city_name):
    city_obj = get_weather_api_data(city_name)
    new_city = City(city_obj['name'], int((city_obj['main']['temp']) - 273), city_obj['weather'][0]['main'])

    return new_city


def show_cities_quantities(weather_list, max_number):
    filtered_weather_list = []

    if max_number > len(weather_list):
        for i in range(len(weather_list)):
            filtered_weather_list.append(weather_list[i])

    if max_number <= len(weather_list):
        for i in range(max_number):
            filtered_weather_list.append(weather_list[i])

    return filtered_weather_list
