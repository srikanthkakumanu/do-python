import httpx
import asyncio


async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.httpbin.org/get")
        print(response.status_code)
        print(response.text)


asyncio.run(main())
