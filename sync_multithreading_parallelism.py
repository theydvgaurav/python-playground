import asyncio
import time
from datetime import datetime
from threading import Thread


def fun1():
    start = datetime.now()
    print("Starting fun1 Execution")
    time.sleep(6)
    end = datetime.now()
    print(f"Time taken for execution of fun1 :: {(end - start).seconds} second(s)")


def fun2():
    start = datetime.now()
    print("Starting fun2 Execution")
    time.sleep(2)
    end = datetime.now()
    print(f"Time taken for execution of fun2 :: {(end - start).seconds} second(s)")


def fun3():
    start = datetime.now()
    print("Starting fun3 Execution")
    time.sleep(3)
    end = datetime.now()
    print(f"Time taken for execution of fun3 :: {(end - start).seconds} second(s)")


async def async_fun1():
    start = datetime.now()
    print("Starting fun1 Execution")
    time.sleep(3)
    await asyncio.sleep(2)
    time.sleep(1)
    end = datetime.now()
    print(f"Time taken for execution of fun1 :: {(end - start).seconds} second(s)")


async def async_fun2():
    start = datetime.now()
    print("Starting fun2 Execution")
    await asyncio.sleep(2)
    end = datetime.now()
    print(f"Time taken for execution of fun2 :: {(end - start).seconds} second(s)")


async def async_fun3():
    start = datetime.now()
    print("Starting fun3 Execution")
    time.sleep(1)
    await asyncio.sleep(2)
    end = datetime.now()
    print(f"Time taken for execution of fun3 :: {(end - start).seconds} second(s)")


def sync_calls():
    start = datetime.now()
    print("Starting Sync Execution of fns")
    fun1()
    fun2()
    fun3()
    end = datetime.now()
    print(f"Time taken for sync execution of fns :: {(end - start).seconds} second(s)")


async def async_calls():
    start = datetime.now()
    print("Starting async Execution of fns")
    tasks = [async_fun1(), async_fun2(), async_fun3()]
    await asyncio.gather(*tasks)
    end = datetime.now()
    print(f"Time taken for async execution of fns :: {(end - start).seconds} second(s)")


def multi_threaded():
    start = datetime.now()
    print("Starting Multi-threaded Execution of fns")
    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)
    t3 = Thread(target=fun3)
    t1.start()
    t2.start()
    t3.start()
    # t1.join()
    # t2.join()
    # t3.join()
    end = datetime.now()
    print(f"Time taken for multi-threaded execution of fns :: {(end - start).seconds} second(s)")


def runner():
    sync_calls()
    print("*********************************")
    asyncio.run(async_calls())
    print("*********************************")
    multi_threaded()


if __name__ == "__main__":
    runner()

# output
"""
Starting Sync Execution of fns
Starting fun1 Execution
Time taken for execution of fun1 :: 6 second(s)
Starting fun2 Execution
Time taken for execution of fun2 :: 2 second(s)
Starting fun3 Execution
Time taken for execution of fun3 :: 3 second(s)
Time taken for sync execution of fns :: 11 second(s)
*********************************
Starting async Execution of fns
Starting fun1 Execution
Starting fun2 Execution
Starting fun3 Execution
Time taken for execution of fun1 :: 6 second(s)
Time taken for execution of fun2 :: 3 second(s)
Time taken for execution of fun3 :: 3 second(s)
Time taken for async execution of fns :: 6 second(s)
*********************************
Starting Multi-threaded Execution of fns
Starting fun1 Execution
Starting fun2 Execution
Starting fun3 Execution
Time taken for multi-threaded execution of fns :: 0 second(s)
Time taken for execution of fun2 :: 2 second(s)
Time taken for execution of fun3 :: 3 second(s)
Time taken for execution of fun1 :: 6 second(s)
"""
