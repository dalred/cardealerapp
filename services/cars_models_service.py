from flask import jsonify
from marshmallow import ValidationError

from dao.models.schemas.schemas import CarModelsSchema
from exceptions import UnknownField
from helpers.functions import set_keys
from services.base_service import BaseService

car_model_schema = CarModelsSchema()
cars_models_schema = CarModelsSchema(many=True)


class Cars_modelsService(BaseService):
    """
    Класс отвечающий за сервис класс cars_models
    """
    def create_cars_models(self, data: dict) -> jsonify:
        try:
            data = car_model_schema.load(data)
        except ValidationError as e:
            raise UnknownField(message=e.normalized_messages())
        models = super().create_models(data)
        return jsonify({"location": f'/cars_models/{models.id}'})


    def update_cars_models(self, data: dict, id: int) -> jsonify:
        try:
            data = car_model_schema.load(data)
        except ValidationError as e:
            raise UnknownField(message=e.normalized_messages())
        update = super().update(id)
        set_keys(data, update)
        self.modeldao.update(update)
        return jsonify({"location": f'/modelscar/{update.id}'})

    def get_all_cars_models(self):
        cars_models = super().get_all_models()
        return cars_models_schema.dump(cars_models)


    def get_cars_models_by_id(self, id: int):
        cars_models = super().get_item_by_id(id)
        return car_model_schema.dump(cars_models)
