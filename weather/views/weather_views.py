from flask import Blueprint, Flask, request
from json import dumps
from http import HTTPStatus

from weather.services.weather_data import show_cities_quantities, selected_response
from weather.services.http import build_api_response, build_response_message
from weather.ext import cache


bp_weather_api = Blueprint('weather_api', __name__)

weather_list = []


@bp_weather_api.route('/weather/<city_name>', methods=["GET"])
@cache.cached(timeout=300)
def get_city_name(city_name):

    try:
        data = selected_response(city_name).__dict__

        if len(weather_list) >= 5:
            weather_list.insert(0, data)
            weather_list.pop(5)

        if len(weather_list) < 5:
            weather_list.insert(0, data)

        return dumps(data)
    except Exception as error:
        print(error)
        return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_weather_api.route('/weather', methods=["GET"])
def get_all_cities():
    try:
        max_number = int(request.args['max'])

        if max_number > 5:
            return {'error': 'max number is 5'}, HTTPStatus.BAD_REQUEST

        data = show_cities_quantities(
            max_number=max_number, weather_list=weather_list)

        return dumps(data)
    except Exception as error:
        print(error)
        return build_api_response(HTTPStatus.BAD_REQUEST)
