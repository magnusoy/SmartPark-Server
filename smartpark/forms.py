#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from smartpark import app
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = TextField("Name",  [validators.Required("Please enter your name.")])
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
    message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")
