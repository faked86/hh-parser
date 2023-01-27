import asyncio

import aiohttp
import pydantic


class HTMLTuple(pydantic.BaseModel):
    HTMLs: tuple


async def _download_page(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as resp:
        return await resp.text()


async def download(base_url: str, page_count: int) -> HTMLTuple:
    async with aiohttp.ClientSession() as session:
        tasks: list[asyncio.Task] = []
        for i in range(page_count):
            page_number = i + 1
            url = (base_url + "&page={page}").format(page=page_number)
            tasks.append(asyncio.create_task(_download_page(session, url)))
        htmls = await asyncio.gather(*tasks)
        return HTMLTuple(HTMLs=tuple(htmls))


if __name__ == "__main__":
    asyncio.run(
        download(
            "https://novosibirsk.hh.ru/search/vacancy?only_with_salary=true&text=%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D1%8B%D0%B9+%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA",
            11,
        )
    )
