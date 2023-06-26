import asyncio

async def fun1():
    await asyncio.sleep(1)
    return "Result 1"

async def fun2():
    await asyncio.sleep(2)
    return "Result 2"

async def fun3():
    await asyncio.sleep(3)
    return "Result 3"

async def main():
    tasks = [fun1(), fun2(), fun3()]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
