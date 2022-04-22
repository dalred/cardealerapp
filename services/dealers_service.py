from flask import jsonify
from marshmallow import ValidationError

from models.schemas.schemas import DealerSchema
from exceptions import UnknownField
from helpers.functions import set_keys
from services.base_service import BaseService

dealer_schema = DealerSchema()
dealers_schema = DealerSchema(many=True)


class DealersService(BaseService):
    """
    Класс отвечающий за сервис класс dealers
    """
    def create_dealer(self, data: dict) -> jsonify:
        try:
            data = dealer_schema.load(data)
        except ValidationError as e:
            raise UnknownField(message=e.normalized_messages())
        models = super().create_models(data)
        return jsonify({"location": f'/dealers/{models.id}'})


    def update_dealer(self, data: dict, id: int) -> jsonify:
        try:
            data = dealer_schema.load(data)
        except ValidationError as e:
            raise UnknownField(message=e.normalized_messages())
        update = super().update(id)
        set_keys(data, update)
        self.modeldao.update(update)
        return jsonify({"location": f'/dealers/{update.id}'})

    def get_all_dealers(self) -> dict:
        dealers_models = super().get_all_models()
        return dealers_schema.dump(dealers_models)


    def get_dealer_by_id(self, id: int) -> dict:
        dealers_models = super().get_item_by_id(id)
        return dealer_schema.dump(dealers_models)
