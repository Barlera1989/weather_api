from flask import Flask


def config_views(app: Flask):

    from .weather_views import bp_all_cities, bp_city_name, bp_teste
    app.register_blueprint(bp_all_cities)
    app.register_blueprint(bp_city_name)
    app.register_blueprint(bp_teste)
