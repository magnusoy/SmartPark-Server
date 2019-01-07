#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import request, render_template, flash
from ..forms import ContactForm
from smartpark import app
from smartpark import mail, Message

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/overview')
def overview():
    return render_template("overview.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
     
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['magnus.oye@gmail.com'])
            msg.body = """
            From: %s, %s;
            
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
 
    elif request.method == 'GET':
        return render_template('contact.html', form=form)
