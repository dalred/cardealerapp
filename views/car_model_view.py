from flask import request
from flask_restx import abort, Namespace, Resource

from exceptions import ItemNotFound, UnknownField
from implemented import car_model_service

cars_models_ns = Namespace("modelscar")


@cars_models_ns.route("/")
class CarsModelView(Resource):
    @cars_models_ns.response(200, "OK")
    def get(self):
        """Get all CarsModel"""
        return car_model_service.get_all_cars_models()

    def post(self):
        """Create car_models"""
        req_json = request.json
        try:
            return car_model_service.create_car_models(req_json)
        except UnknownField as e:
            abort(502, message=e.message)

@cars_models_ns.route('/<int:id>/')
class Car_modelView(Resource):
    @cars_models_ns.response(200, "OK")
    @cars_models_ns.response(404, "Car_model not found")
    def get(self, id: int):
        try:
            return car_model_service.get_car_models_by_id(id)
        except ItemNotFound as e:
            abort(404, message=e.message)

    def patch(self, id: int):
        req_json = request.json
        try:
            car_model_service.update_car_models(req_json, id)
        except UnknownField as e:
            abort(502, message=e.message)
        return "", 204

    def delete(self, id: int):
        try:
            car_model_service.delete(id)
        except ItemNotFound as e:
            abort(404, message=e.message)
        return "", 204
