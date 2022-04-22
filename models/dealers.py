import datetime
from dataclasses import dataclass

from setup_db import db


@dataclass
class Dealer(db.Model):
    id: int
    name: str
    address: str
    phone: str
    email: str

    __tablename__ = 'dealers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)
