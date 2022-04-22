from flask import jsonify
from marshmallow import ValidationError

from dao.models.schemas.schemas import CarSchema
from exceptions import UnknownField
from helpers.functions import set_keys
from services.base_service import BaseService

carschema = CarSchema()
carsschema = CarSchema(many=True)


class CarsService(BaseService):
    """
    Класс отвечающий за сервис класс cars_models
    """
    def create_car(self, data: dict) -> jsonify:
        try:
            data = carschema.load(data)
        except ValidationError as e:
            raise UnknownField(message=e.normalized_messages())
        models = super().create_models(data)
        return jsonify({"location": f'/cars_models/{models.id}'})


    def update_car(self, data: dict, id: int) -> jsonify:
        try:
            data = carschema.load(data)
        except ValidationError as e:
            raise UnknownField(message=e.normalized_messages())
        update = super().update(id)
        set_keys(data, update)
        self.modeldao.update(update)
        return jsonify({"location": f'/modelscar/{update.id}'})

    def get_all_cars(self) -> dict:
        cars_models = super().get_all_models()
        return carsschema.dump(cars_models)


    def get_car_by_id(self, id: int) -> dict:
        cars_models = super().get_item_by_id(id)
        return carschema.dump(cars_models)
