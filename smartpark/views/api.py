#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from smartpark import app
from flask import request, jsonify, make_response
from smartpark.models import Parkinglot
from smartpark import ma
from smartpark import db
from functools import wraps
import os.path
import json
import datetime
import jwt


class ParkinglotSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'name', 'location', 'size', 'empty')


parkinglot_schema = ParkinglotSchema()
parkinglots_schema = ParkinglotSchema(many=True)
if not os.path.isfile("../instance/crud.sqlite"):
    db.create_all()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorated


@app.route('/unprotected')
def unprotected():
    return jsonify({'message': 'Anyone can view this!'})


@app.route('/protected')
@token_required
def protected():
    return jsonify({'message': 'This is only available for people with valid tokens.'})


@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(days=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


# endpoint to create new parkinglot
@app.route("/parkinglots", methods=["POST"])
@token_required
def add_parkinglot():
    name = request.json['name']
    location = request.json['location']
    size = request.json['size']
    empty = request.json['empty']

    new_parkinglot = Parkinglot(name, location, size, empty)

    db.session.add(new_parkinglot)
    db.session.commit()
    return parkinglot_schema.jsonify(new_parkinglot)


# endpoint to show all parkinglots
@app.route("/parkinglots", methods=["GET"])
def get_parkinglot():
    all_parkinglots = Parkinglot.query.all()
    result = parkinglots_schema.dump(all_parkinglots)
    return jsonify(result.data)


# endpoint to get parkinglot detail by id
@app.route("/parkinglots/<id>", methods=["GET"])
def detail_parkinglot(id):
    parkinglot = Parkinglot.query.get(id)
    return parkinglot_schema.jsonify(parkinglot)


# endpoint to update parkinglot
@app.route("/parkinglots/<id>", methods=["PUT"])
@token_required
def update_parkinglot(id):
    parkinglot = Parkinglot.query.get(id)
    name = request.json['name']
    location = request.json['location']
    size = request.json['size']
    empty = request.json['empty']

    parkinglot.name = name
    parkinglot.location = location
    parkinglot.size = size
    parkinglot.empty = empty
    db.session.commit()
    return parkinglot_schema.jsonify(parkinglot)


# endpoint to delete parkinglot
@app.route("/parkinglots/<id>", methods=["DELETE"])
@token_required
def delete_parkinglot(id):
    parkinglot = Parkinglot.query.get(id)
    db.session.delete(parkinglot)
    db.session.commit()

    return parkinglot_schema.jsonify(parkinglot)
