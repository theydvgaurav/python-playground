import asyncio
from datetime import datetime

import requests


def make_sync_call(pid):
    response = requests.get(f'https://dummyapi.online/api/pokemon/{pid}')
    if response.status_code == 200:
        return response.json().get("pokemon")


async def make_async_call(pid):
    return await asyncio.to_thread(make_sync_call, pid)


def sync_call():
    print("Started Sync Call")
    st = datetime.now()
    print([make_sync_call(pid) for pid in range(1, 20)])
    print(f"Took: {datetime.now() - st}")


async def runner():
    r = await asyncio.gather(*[make_async_call(pid) for pid in range(1, 20)])
    print(r)


def async_call():
    print("Started Async Call")
    st = datetime.now()
    asyncio.run(runner())
    print(f"Took: {datetime.now() - st}")


if __name__ == "__main__":
    sync_call()
    async_call()
