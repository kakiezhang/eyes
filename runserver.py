# -*- encoding: utf8 -*-
import os
import views
from application import app

if __name__ == '__main__' :
    app.run(host="0.0.0.0", port=5021, debug=True)

