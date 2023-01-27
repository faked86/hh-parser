import asyncio

from src.downloader import download


if __name__ == "__main__":
    # TODO: custom query builder
    print(
        """1. Go to hh.ru
2. Enter vacancy name
3. Press `Enter`
4. Change filters
5. Copy URL
6. Check count of pages
"""
    )

    base_url = input("Enter copied URL: ")
    page_number = int(input("Enter number of pages: "))

    htmls = asyncio.run(
        download(
            base_url,
            page_number,
        )
    )
