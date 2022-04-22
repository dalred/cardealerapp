from flask import request
from flask_restx import abort, Namespace, Resource

from exceptions import ItemNotFound, UnknownField
from implemented import car_service

cars_ns = Namespace("cars")


@cars_ns.route("/")
class CarsView(Resource):
    @cars_ns.response(200, "OK")
    def get(self):
        """Get all Car"""
        return car_service.get_all_cars()

    def post(self):
        """Create car"""
        req_json = request.json
        try:
            return car_service.create_car(req_json)
        except UnknownField as e:
            abort(502, message=e.message)

@cars_ns.route('/<int:id>/')
class CarView(Resource):
    @cars_ns.response(200, "OK")
    @cars_ns.response(404, "Car not found")
    def get(self, id: int):
        try:
            return car_service.get_car_by_id(id)
        except ItemNotFound as e:
            abort(404, message=e.message)

    def patch(self, id: int):
        req_json = request.json
        try:
            car_service.update_car(req_json, id)
        except UnknownField as e:
            abort(502, message=e.message)
        return "", 204

    def delete(self, id: int):
        try:
            car_service.delete(id)
        except ItemNotFound as e:
            abort(404, message=e.message)
        return "", 204
