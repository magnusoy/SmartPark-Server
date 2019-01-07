#!flask/bin/python3
# -*- coding: utf-8 -*-

from smartpark import app

DEBUG = False

app.run(
        debug=DEBUG,
        host='0.0.0.0',
        threaded=True
    )
