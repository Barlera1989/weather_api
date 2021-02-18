from dynaconf import FlaskDynaconf
from flask import Flask
from importlib import import_module


def init_app(app: Flask, **kwargs):
    FlaskDynaconf(
        app,
        settings_files=['settings.toml', '.secrets.toml'],
        **kwargs
    )


def load_extensions(app: Flask):
    extension_list = app.config.get('EXTENSIONS')

    for extension in extension_list:
        module = import_module(extension)
        module.init_app(app)
