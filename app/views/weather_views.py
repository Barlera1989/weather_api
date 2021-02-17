from flask import Blueprint, Flask, request
from app.services.weather_data import show_cities_quantities, selected_response
from json import dumps
from app import cache
from app.services.http import build_api_response, build_response_message
from http import HTTPStatus


bp_all_cities = Blueprint('all_blueprint', __name__)
bp_city_name = Blueprint('cities_blueprint', __name__)
bp_teste = Blueprint('teste_blueprint', __name__)

weather_list = []


@bp_city_name.route('/weather/<city_name>', methods=["GET"])
@cache.cached(timeout=300)
def get(city_name):

    try:
        data = selected_response(city_name).data_dict()

        if len(weather_list) >= 5:
            weather_list.insert(0, data)
            weather_list.pop(5)

        if len(weather_list) < 5:
            weather_list.insert(0, data)

        return dumps(data)
    except:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_all_cities.route('/weather', methods=["GET"])
def get():

    try:
        max_number = int(request.args['max'])

        if max_number > 5:
            return {'error': 'max number is 5'}, HTTPStatus.BAD_REQUEST

        data = show_cities_quantities(
            max_number=max_number, weather_list=weather_list)

        return dumps(data)
    except:
        return build_api_response(HTTPStatus.BAD_REQUEST)
