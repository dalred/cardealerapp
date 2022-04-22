import os
from config import BASEDIR
from dao.CarDAO import CarDAO
from dao.Car_ModelsDAO import Car_ModelsDAO
from dao.CountryDAO import CountryDAO
from dao.modelDAO import DealerDAO
from dao.models import Country, Car_Model, Car, Dealer
from helpers import read_json
from services.cars_models_service import Cars_modelsService
from services.cars_service import CarsService
from services.countries_service import CountriesService
from services.dealers_service import DealersService
from setup_db import db

path = os.path.join(BASEDIR, 'data')

cars_dict: dict = read_json(f'{path}/cars.json')
countries_dict: dict = read_json(f'{path}/countries.json')
car_models_dict: dict = read_json(f'{path}/car_models.json')
dealers_dict: dict = read_json(f'{path}/dealers.json')

countries = CountryDAO(db.session, Country)
country_service = CountriesService(db.session, countries)

cars_models = Car_ModelsDAO(db.session, Car_Model)
car_model_service = Cars_modelsService(db.session, cars_models)

cars = CarDAO(db.session, Car)
car_service = CarsService(db.session, cars)


dealers = DealerDAO(db.session, Dealer)
dealer_service = DealersService(db.session, dealers)