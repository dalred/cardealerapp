from flask import jsonify
from marshmallow import ValidationError

from dao.models.schemas.schemas import CountrySchema
from exceptions import UnknownField
from helpers.functions import set_keys
from services.base_service import BaseService

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)


class CountriesService(BaseService):
    """
    Класс отвечающий за сервис класс country
    """
    def create_country(self, data: dict) -> jsonify:
        try:
            data = country_schema.load(data)
        except ValidationError as e:
            raise UnknownField(message=e.normalized_messages())
        models = super().create_models(data)
        return jsonify({"location": f'/countries/{models.id}'})


    def update_country(self, data: dict, id: int) -> jsonify:
        try:
            data = country_schema.load(data)
        except ValidationError as e:
            raise UnknownField(message=e.normalized_messages())
        update = super().update(id)
        set_keys(data, update)
        self.modeldao.update(update)
        return jsonify({"location": f'/countries/{update.id}'})

    def get_all_countries(self):
        countries = super().get_all_models()
        return countries_schema.dump(countries)


    def get_country_by_id(self, id: int):
        country = super().get_item_by_id(id)
        return country_schema.dump(country)
