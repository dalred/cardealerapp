from dao.models.models_options.car_model_options import Car_Models_Option
from dao.models.models_options.cars_options import Cars_Option
from dao.models.models_options.countries_options import Country_Option
from dao.models.models_options.dealers_options import Dealer_Option
from implemented import cars_dict, countries_dict, car_models_dict, dealers_dict
from setup_db import db
from dao.models import *

def create_tables():
    db.drop_all()
    db.create_all()
    country = Country_Option(Country)
    country = country.load_schema(countries_dict, many=True)

    car_model = Car_Models_Option(Car_Model)
    car_model = car_model.load_schema(car_models_dict, many=True)

    car = Cars_Option(Car)
    car = car.load_schema(cars_dict, many=True)

    dealer = Dealer_Option(Dealer)
    dealer = dealer.load_schema(dealers_dict, many=True)

    db.session.add_all(country)
    db.session.add_all(car_model)
    db.session.add_all(dealer)
    db.session.add_all(car)
    db.session.commit()
    # users = Users_Option(User, users_dict)
    # weapons = Weapons_Option(Weapon, eq_dict)
    # db.session.add_all(users.load_schema(users_dict, many=True))
    # db.session.add_all(weapons.load_schema(eq_dict, many=True))
    # db.session.commit()
