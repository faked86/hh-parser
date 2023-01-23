from src.interfaces.browser_interface import BrowserInterface


DEFAULT_BATCH_SIZE = 5


class PlaywrightAdapter(BrowserInterface):
    """Browser adapter for playwright."""

    def __init__(self, vacancy: str, batch_size: int = DEFAULT_BATCH_SIZE) -> None:
        pass

    async def __aiter__(self):
        pass
