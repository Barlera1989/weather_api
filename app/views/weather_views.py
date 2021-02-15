from flask import Blueprint, Flask, request

bp_all_cities = Blueprint('all_blueprint', __name__)
bp_city_name = Blueprint('cities_blueprint', __name__)


@bp_all_cities.route('/weather/all', methods=["GET"])
def get():
    return {'message': 'ok'}


@bp_city_name.route('/weather/cities', methods=["GET"])
def get():
    return {'message': 'done!'}
