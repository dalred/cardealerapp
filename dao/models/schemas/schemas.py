# На данный момент нереализованный функционал
import datetime

from marshmallow import Schema, fields

from marshmallow.fields import Int, Boolean, Decimal, DateTime, Str


class CountrySchema(Schema):
    id = Int(dump_only=True)  # Пропускаем поле id для дессерилиазации(для load)
    name = Str()


class CarModelsSchema(Schema):
    id = Int(dump_only=True)  # Пропускаем поле id для дессерилиазации(для load)
    brand = Str()
    name = Str()
    country = fields.Nested(CountrySchema, dump_only=True)
    # Для вложенной схемы название
    # должно обязательно совпадать с названием в модели relationship

class DealerSchema(Schema):
    id = Int(dump_only=True)  # Пропускаем поле id для дессерилиазации(для load)
    name = Str()
    address = Str()
    phone = Str()
    email = Str()

class CarSchema(Schema):
    id = Int(dump_only=True)  # Пропускаем поле id для дессерилиазации(для load)
    model_id = Int()
    dealer_id = Int()
    year = DateTime(load_default=datetime.datetime.now())
    name = Str()
    price = Decimal(as_string=True)
    is_sold = Boolean()
    car_model = fields.Nested(CarModelsSchema, dump_only=True)
    dealer = fields.Nested(DealerSchema, dump_only=True)

