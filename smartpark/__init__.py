#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mail import Message, Mail

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

mail = Mail()
mail.init_app(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

from smartpark.views import webpage
from smartpark.views import api
