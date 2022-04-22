from dataclasses import dataclass
from typing import List
from setup_db import db


@dataclass
class Weapon(db.Model):
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float
    user_id: int

    __tablename__ = 'weapons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    min_damage = db.Column(db.Float())
    max_damage = db.Column(db.Float())
    stamina_per_hit = db.Column(db.Float())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


# @dataclass
# class WeponsData:
#     weapons: List[Weapon]
