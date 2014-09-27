# -*- encoding: utf8 -*-

from flask import Flask
from config.config import config

app = Flask(__name__, template_folder=config.TEMPLATE_FOLDER, static_folder=config.STATIC_FOLDER)

