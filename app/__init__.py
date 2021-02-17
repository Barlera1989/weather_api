from flask import Flask
from app.views import config_views
from flask_caching import Cache
from flask_cors import CORS

cache = Cache(config={'CACHE_TYPE': 'simple'})


def create_app():
    app = Flask(__name__)
    CORS(app)

    cache.init_app(app)
    app.cache = cache
    client = app.test_client()
    app.testing = True

    config_views(app)

    return app
