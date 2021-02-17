from flask import Blueprint, Flask, request
from app.services.weather_data import show_cities_quantities, selected_response
from json import dumps
from app import cache

bp_all_cities = Blueprint('all_blueprint', __name__)
bp_city_name = Blueprint('cities_blueprint', __name__)
bp_teste = Blueprint('teste_blueprint', __name__)

weather_list = []


@bp_city_name.route('/weather/<city_name>', methods=["GET"])
@cache.cached(timeout=15)
def get(city_name):

    data = selected_response(city_name).data_dict()

    if len(weather_list) >= 5:
        weather_list.insert(0, data)
        weather_list.pop(5)

    if len(weather_list) < 5:
        weather_list.insert(0, data)

    return dumps(data)


@bp_all_cities.route('/weather', methods=["GET"])
def get():

    max_number = int(request.args['max'])

    if max_number > 5:
        return {'error': 'the specified number is higher than existing cities'}

    data = show_cities_quantities(
        max_number=max_number, weather_list=weather_list)

    return dumps(data)


@bp_teste.route('/teste', methods=["GET"])
def get():

    return dumps(weather_list)
