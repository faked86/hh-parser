import asyncio

from src.downloader import download


if __name__ == "__main__":
    htmls = asyncio.run(
        download(
            "https://novosibirsk.hh.ru/search/vacancy?only_with_salary=true&text=%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D1%8B%D0%B9+%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA",
            11,
        )
    )

    for i, html in enumerate(htmls.HTMLs):
        with open(f"htmls/{i}.html", "w") as f:
            f.write(html)
