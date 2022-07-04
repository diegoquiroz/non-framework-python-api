import enum

from typing import Optional
from utils import PropertyRepositoryMySQL


class property_statuses(enum.Enum):
    COMPRANDO = 1, 'comprando'
    COMPRADO = 2, 'comprado'
    PRE_VENTA = 3, 'pre_venta'
    EN_VENTA = 4, 'en_venta'
    VENDIDO = 5, 'vendido'


class Property:
    id: int
    address: str
    city: str
    price: int
    description: Optional[str] = None
    year: Optional[int] = None
    status: str

    def filter(self, **kwargs: str) -> list:
        return PropertyRepositoryMySQL.list(**kwargs)
