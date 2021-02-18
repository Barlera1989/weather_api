from flask import Flask

from weather import views
from weather.ext import configuration


def simple_app(**kwargs):
    app = Flask(__name__)
    configuration.init_app(app, **kwargs)

    return app


def create_app(**kwargs):
    app = simple_app(**kwargs)
    configuration.load_extensions(app)

    return app
