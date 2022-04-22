import datetime
from dataclasses import dataclass

from setup_db import db


@dataclass
class Car_Model(db.Model):
    id: int
    brand: str
    name: str
    country_id: int

    __tablename__ = 'car_models'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String)
    name = db.Column(db.String)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    country = db.relationship('Country')