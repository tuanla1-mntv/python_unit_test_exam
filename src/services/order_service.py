from typing import List
import time

from constants.constants import (
    OrderType,
    OrderStatus,
    OrderPriority,
    APIStatus,
    OrderAmountThreshold,
    ORDER_API_RESPONSE_THRESHOLD,
)
from models.order_model import Order
from utils.exporters.csv_exporter import CSVExporter
from utils.exceptions.database_exception import DatabaseException
from utils.exceptions.api_exception import APIException
from routers.order_api_client import OrderAPIClient


class OrderService:

    @classmethod
    def fetch_orders_by_user(cls, user_id: int) -> List[Order]:
        """Fetch orders for a specific user.

        Args:
                user_id (int): ID of the user

        Returns:
                List[Order]: List of orders for the user

        Raises:
                DatabaseException: If there's an error accessing the database
        """
        pass

    @classmethod
    def update_order(cls, order: Order) -> bool:
        """Update the status and priority of an order.

        Args:
                order (Order): Order object to be updated

        Returns:
                bool: True if update was successful, False otherwise

        Raises:
                DatabaseException: If there's an error updating the database
        """
        pass

    @classmethod
    def process_order_by_user_id(cls, user_id: int) -> bool:
        """Process orders for a specific user.

        Args:
                user_id (int): ID of the user

        Raises:
                DatabaseException: If there's an error accessing the database
        """
        try:
            orders = cls.fetch_orders_by_user(user_id)
            return cls.process_orders(orders, user_id)
        except DatabaseException:
            return False

    @classmethod
    def process_orders(cls, orders: List[Order], user_id: int = None) -> bool:
        """Process a list of orders.

        Args:
                orders (List[Order]): List of orders to be processed

        Returns:
                bool: True if processing was successful, False otherwise
        """
        try:
            for order in orders:
                if order.type == OrderType.A:
                    cls.process_type_a_orders(order, user_id)

                elif order.type == OrderType.B:
                    cls.process_type_b_orders(order)

                elif order.type == OrderType.C:
                    cls.process_type_c_orders(order)

                else:
                    order.status = OrderStatus.UNKNOWN_TYPE

                # Set priority based on amount
                if order.amount > OrderAmountThreshold.PRIORITY_THRESHOLD:
                    order.priority = OrderPriority.HIGH
                else:
                    order.priority = OrderPriority.LOW

                # Attempt to update the order in the database
                try:
                    cls.update_order(order)
                except DatabaseException:
                    order.status = OrderStatus.DB_ERROR  # Use enum for consistency

            return True
        except Exception:
            return False

    @classmethod
    def process_type_a_orders(cls, order: Order, user_id: int) -> Order:
        """Process orders of type A."""
        csv_file = f"orders_type_A_{user_id}_{int(time.time())}.csv"

        try:
            columns = ["ID", "Type", "Amount", "Is Special", "Status", "Priority"]
            data = [
                columns,
                [
                    order.id,
                    order.type,
                    order.amount,
                    str(order.is_special).lower(),
                    order.status,
                    order.priority,
                ],
            ]

            if order.amount > OrderAmountThreshold.HIGH_VALUE_ORDER_THRESHOLD:
                data.append(["", "", "", "", "Note", "High value order"])
            CSVExporter.export(csv_file, data, columns=columns)

            order.status = OrderStatus.EXPORTED
        except IOError:
            order.status = OrderStatus.EXPORT_FAILED

        return order

    @classmethod
    def process_type_b_orders(cls, order: Order) -> Order:
        """Process orders of type B."""
        try:
            api_client = OrderAPIClient()
            api_response = api_client.call_api(order.id)

            if api_response.status == APIStatus.SUCCESS:
                if (
                    api_response.data >= ORDER_API_RESPONSE_THRESHOLD
                    and order.amount < OrderAmountThreshold.PROCESSED_ORDER_THRESHOLD
                ):
                    order.status = OrderStatus.PROCESSED
                elif (
                    api_response.data < ORDER_API_RESPONSE_THRESHOLD or order.is_special
                ):
                    order.status = OrderStatus.PENDING
                else:
                    order.status = OrderStatus.ERROR
            else:
                order.status = OrderStatus.API_ERROR
        except APIException:
            order.status = OrderStatus.API_FAILURE

        return order

    @classmethod
    def process_type_c_orders(cls, order: Order) -> Order:
        """Process orders of type C."""
        if order.is_special:
            order.status = OrderStatus.COMPLETED
        else:
            order.status = OrderStatus.IN_PROGRESS

        return order
