from flask import request
from flask_restx import abort, Namespace, Resource

from exceptions import ItemNotFound, UnknownField
from implemented import dealer_service

dealers_ns = Namespace("dealers")


@dealers_ns.route("/")
class DealersView(Resource):
    @dealers_ns.response(200, "OK")
    def get(self):
        """Get all Car"""
        return dealer_service.get_all_dealers()

    def post(self):
        """Create dealer"""
        req_json = request.json
        try:
            return dealer_service.create_dealer(req_json)
        except UnknownField as e:
            abort(502, message=e.message)

@dealers_ns.route('/<int:id>/')
class CarView(Resource):
    @dealers_ns.response(200, "OK")
    @dealers_ns.response(404, "Car not found")
    def get(self, id: int):
        try:
            return dealer_service.get_dealer_by_id(id)
        except ItemNotFound as e:
            abort(404, message=e.message)

    def patch(self, id: int):
        req_json = request.json
        try:
            dealer_service.update_dealer(req_json, id)
        except UnknownField as e:
            abort(502, message=e.message)
        return "", 204

    def delete(self, id: int):
        try:
            dealer_service.delete(id)
        except ItemNotFound as e:
            abort(404, message=e.message)
        return "", 204
