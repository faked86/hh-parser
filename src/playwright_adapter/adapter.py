from src.interfaces.adapters.browser_interface import BrowserInterface


DEFAULT_BATCH_SIZE = 5


class PlaywrightAdapter(BrowserInterface):
    """Browser adapter for playwright."""

    def __init__(self, vacancy: str, batch_size: int = DEFAULT_BATCH_SIZE) -> None:
        pass

    def __iter__(self):
        pass
