from abc import ABC, abstractmethod

from responses.api_response import APIResponse


class BaseAPIClient(ABC):
    @abstractmethod
    def call_api(self, *args, **kwargs) -> APIResponse:
        pass
