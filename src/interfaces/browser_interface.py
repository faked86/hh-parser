from abc import ABC, abstractmethod


class BrowserInterface(ABC):
    """Interface to interact with browser adapters."""

    @abstractmethod
    async def __aiter__(self):
        pass