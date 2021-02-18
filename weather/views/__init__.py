from flask import Flask


def init_app(app: Flask):
    from .weather_views import bp_weather_api
    app.register_blueprint(bp_weather_api)
