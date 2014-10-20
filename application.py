# -*- encoding: utf8 -*-

from flask import Flask
from config.config import config

def createApp():
    app = Flask(__name__, template_folder=config.TEMPLATE_FOLDER, static_folder=config.STATIC_FOLDER)

    app.config.from_object(config)
    app.template_folder = app.config['TEMPLATE_FOLDER']
    app.static_folder = app.config['STATIC_FOLDER']

    return app

app = createApp()

