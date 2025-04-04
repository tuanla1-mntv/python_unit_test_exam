from abc import ABC, abstractmethod


class BaseExporter(ABC):
    """Abstract base class for all exporters in the application."""

    @abstractmethod
    def export(data, savedir: str, *args, **kwargs) -> None:
        """Export data to a specified file format."""
        pass
