# coding=utf-8
from flask import Flask
from flask.ext.moment import Moment
from flask_cache import Cache
from config import config


moment = None
cache = None
app = None


def create_app(config_name='default'):
    app = Flask(__name__)
    if config_name.lower() == 'testing':
        app.config['TESTING'] = True

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment = Moment(app)
    moment.init_app(app)

    cache = Cache(app)

    return app
