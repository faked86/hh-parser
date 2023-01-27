import asyncio

from src.downloader import download


if __name__ == "__main__":
    # TODO: custom query builder
    print(
        "1. Go to hh.ru\n"
        "2. Enter vacancy name\n"
        "3. Press `Enter`\n"
        "4. Change filters\n"
        "5. Copy URL\n"
        "6. Check count of pages\n"
    )

    base_url = input("Enter copied URL: ")
    page_number = int(input("Enter number of pages: "))

    htmls = asyncio.run(
        download(
            base_url,
            page_number,
        )
    )
