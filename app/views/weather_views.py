from flask import Blueprint, Flask, request
from app.services.weather_data import get_weather_api_data

bp_all_cities = Blueprint('all_blueprint', __name__)
bp_city_name = Blueprint('cities_blueprint', __name__)


@bp_city_name.route('/weather/cities', methods=["GET"])
def get():
    return {'message': 'done!'}


@bp_all_cities.route('/weather/all', methods=["GET"])
def get():
    data = get_weather_api_data()
    print(data.__dict__)
    return {'message': 'ok'}
