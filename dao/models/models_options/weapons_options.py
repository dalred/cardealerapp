from typing import List, Optional

from dao.models.equipment_model import Weapon
from dao.models.models_options.base_schema import Base_data


class Weapons_Option(Base_data):
    """
    Класс отвечающий за снаряжения игрока
    """
    def __init__(self, object_dataclass, data: Optional[dict] = None):
        super().__init__(object_dataclass)
        self.data = data

    def get_by_id(self, id: int) -> Weapon:
        for item in self.load_schema(self.data, many=True):
            if item.id == id:
                return item
