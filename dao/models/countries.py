import datetime
from dataclasses import dataclass


from setup_db import db


@dataclass
class Country(db.Model):
    id: int
    name: str

    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)