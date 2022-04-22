from models import Country
from models.models_options.base_schema import Base_data
from typing import Optional

class Country_Option(Base_data):
    """
    Класс отвечающий получение экземляров класса Country
    """
    def __init__(self, object_dataclass, data: Optional[dict] = None):
        super().__init__(object_dataclass)
        self.data = data

    def get_by_id(self, id: int) -> Country:
        for item in self.load_schema(self.data, many=True):
            if item.id == id:
                return item