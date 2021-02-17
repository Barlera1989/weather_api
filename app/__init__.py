from flask import Flask
from app.views import config_views

from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    config_views(app)

    return app
