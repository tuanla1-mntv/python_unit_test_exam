from typing import Any


class APIResponse:
    """Represents a response from an API call.

    Attributes:
            status (str): Status of the API response
            data (Any): Data returned by the API
    """

    def __init__(self, status: str, data: Any) -> None:
        self.status = status
        self.data = data
