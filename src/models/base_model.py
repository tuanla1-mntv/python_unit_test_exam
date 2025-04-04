from abc import ABC, abstractmethod


class BaseModel(ABC):
    """Abstract base class for all models in the application."""

    @abstractmethod
    def __init__(self, **kwargs):
        """Initialize the model instance with provided attributes."""
        pass
