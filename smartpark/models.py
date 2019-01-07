from smartpark import app
from . import db

class Parkinglot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    empty = db.Column(db.Integer, nullable=False)

    def __init__(self, name, location, size, empty):
        self.name = name
        self.location = location
        self.size = size
        self.empty = empty
