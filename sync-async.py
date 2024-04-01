# sync async
import asyncio


# async function
async def my_fun(x, y):
    return x + y


# async function
async def fun():
    x = await my_fun(2, 3)  # calling an async function inside an async function
    print(x)
    x = x * x
    print(x)


# sync function
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fun())
    loop.close()


main()

# output
"""
5
25
"""
