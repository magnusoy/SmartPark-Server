#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = '-%entuw(c0yrm_tb02aft7z17!v^9ktgrfvzp%4@ut0tw*t(@f'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
    os.path.join(basedir, 'crud.sqlite')

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'yourname@gmail.com'
MAIL_PASSWORD = 'yourpassword'

