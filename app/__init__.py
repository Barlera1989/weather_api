from flask import Flask
from app.views import config_views


def create_app():
    app = Flask(__name__)

    config_views(app)

    return app
