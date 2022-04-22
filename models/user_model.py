from dataclasses import dataclass
from setup_db import db



@dataclass
class User(db.Model):
    id: int
    email: str
    name: str
    age: int

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String())
    age = db.Column(db.Integer)
    weapon = db.relationship('Weapon')


# @dataclass
# class UsersData:
#     users: List[User]
