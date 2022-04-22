from typing import Optional

from models.user_model import User
from models.models_options.base_schema import Base_data


class Users_Option(Base_data):
    """
    Класс отвечающий получение экземляров игрока
    """
    def __init__(self, object_dataclass, data: Optional[dict] = None):
        super().__init__(object_dataclass)
        self.data = data

    def get_by_id(self, id: int) -> User:
        for item in self.load_schema(self.data, many=True):
            if item.id == id:
                return item