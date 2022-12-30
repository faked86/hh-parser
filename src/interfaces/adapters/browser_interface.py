from abc import ABC, abstractmethod


class BrowserInterface(ABC):
    """Interface to interact with browser adapters."""

    @abstractmethod
    def __iter__(self):
        pass
