import unittest
from models.order_model import Order
from constants.constants import OrderStatus, OrderPriority, OrderType


class TestOrderModel(unittest.TestCase):
    def setUp(self):
        self.order = Order(id=1, type=OrderType.A, amount=100.0, is_special=False)

    def test_initialization(self):
        self.assertEqual(self.order.id, 1)
        self.assertEqual(self.order.type, OrderType.A)
        self.assertEqual(self.order.amount, 100.0)
        self.assertFalse(self.order.is_special)
        self.assertEqual(self.order.status, OrderStatus.NEW)
        self.assertEqual(self.order.priority, OrderPriority.LOW)


if __name__ == "__main__":
    unittest.main()
