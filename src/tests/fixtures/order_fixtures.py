from models.order_model import Order
from constants.constants import OrderType, OrderPriority


def get_valid_order_fixture():
    """Returns a valid order with OrderType A and LOW priority."""
    return Order(id=1, type=OrderType.A, amount=100.0, is_special=False)


def get_high_priority_order_fixture():
    """Returns a valid order with OrderType B and HIGH priority."""
    order = Order(id=2, type=OrderType.B, amount=200.0, is_special=True)
    order.priority = OrderPriority.HIGH
    return order


def get_invalid_type_order_fixture():
    """Returns an order with an invalid OrderType."""
    return Order(id=3, type="INVALID_TYPE", amount=50.0, is_special=False)
