from flask_cors import CORS
from flask import Flask


def init_app(app: Flask):
    CORS(app)
