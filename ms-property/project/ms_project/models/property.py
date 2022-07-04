from typing import Optional
from utils import PropertyRepositoryMySQL


class Property:
    id: int
    address: str
    city: str
    price: int
    description: Optional[str] = None
    year: Optional[int] = None

    def filter(*args) -> list:
        return PropertyRepositoryMySQL.list()
