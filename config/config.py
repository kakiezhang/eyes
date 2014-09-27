# -*- encoding: utf8 -*-

import os

root_path = os.path.dirname(os.path.abspath(__file__))+'/../'
print root_path

class Config() :
    
    TEMPLATE_FOLDER = root_path + "templates"
    STATIC_FOLDER = root_path + "static"

config = Config()
