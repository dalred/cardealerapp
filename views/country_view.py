from flask import request
from flask_restx import abort, Namespace, Resource

from exceptions import ItemNotFound, UnknownField
from implemented import country_service

countries_ns = Namespace("countries")


@countries_ns.route("/")
class CountriesView(Resource):
    @countries_ns.response(200, "OK")
    def get(self):
        """Get all Countries"""
        return country_service.get_all_countries()

    def post(self):
        """Create country"""
        req_json = request.json
        try:
            return country_service.create_country(req_json)
        except UnknownField as e:
            abort(502, message=e.message)

@countries_ns.route('/<int:id>/')
class CountryView(Resource):
    @countries_ns.response(200, "OK")
    @countries_ns.response(404, "Country not found")
    def get(self, id: int):
        try:
            return country_service.get_country_by_id(id)
        except ItemNotFound as e:
            abort(404, message=e.message)

    def patch(self, id: int):
        req_json = request.json
        try:
            country_service.update_country(req_json, id)
        except UnknownField as e:
            abort(502, message=e.message)
        return "", 204

    def delete(self, id: int):
        try:
            country_service.delete(id)
        except ItemNotFound:
            abort(404, message="Country not found")
        return "", 204
