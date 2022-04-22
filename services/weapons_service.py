from flask import jsonify
from services.base_service import BaseService


class WeaponsService(BaseService):
    def create_models(self, data: dict) -> jsonify:
        models = super().create_models(data)
        return jsonify({"location": f'/weapons/{models.id}'})
