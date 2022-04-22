import datetime
from dataclasses import dataclass

from setup_db import db
from decimal import Decimal


@dataclass
class Car(db.Model):
    id: int
    model_id: int
    dealer_id: int
    price: Decimal
    is_sold: bool
    year: datetime.datetime

    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model_id = db.Column(db.Integer, db.ForeignKey('car_models.id'))
    dealer_id = db.Column(db.Integer, db.ForeignKey('dealers.id'))
    year = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"
                                                                                            ".%fZ"))
    price = db.Column(db.DECIMAL)
    is_sold = db.Column(db.Boolean)
    car_model = db.relationship('Car_Model')
    dealer = db.relationship('Dealer')
