from constants.constants import OrderStatus, OrderPriority
from .base_model import BaseModel


class Order(BaseModel):
    """Represents an order in the system."""

    def __init__(self, id: int, type: str, amount: float, is_special: bool):
        self.id = id
        self.type = type
        self.amount = amount
        self.is_special = is_special
        self.status = OrderStatus.NEW
        self.priority = OrderPriority.LOW
