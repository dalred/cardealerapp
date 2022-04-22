from models import Car_Model
from models.models_options.base_schema import Base_data
from typing import Optional

class Car_Models_Option(Base_data):
    """
    Класс потомок отвечающий за получение экземляров класса Car_Model
    с различными опциями.
    """
    def __init__(self, object_dataclass, data: Optional[dict] = None):
        super().__init__(object_dataclass)
        self.data = data

    # Вызов метода super() предполагает, возможность вызывать метод
    # get_by_id в потомке уже без передачи словаря.
    def get_by_id(self, id: int) -> Car_Model:
        for item in self.load_schema(self.data, many=True):
            if item.id == id:
                return item

    def test_method(self):
        pass