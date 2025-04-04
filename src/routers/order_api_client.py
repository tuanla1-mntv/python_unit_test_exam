from responses.api_response import APIResponse
from .base_api_client import BaseAPIClient


class OrderAPIClient(BaseAPIClient):
    """Client for order-related API calls."""

    def call_api(self, order_id: int) -> APIResponse:
        pass
