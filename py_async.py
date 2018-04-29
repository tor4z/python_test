import random
import asyncio
from asyncio.futures import Future
from asyncio.coroutines import coroutine
import time

@coroutine
def my_sleep(t):
    loop = asyncio.get_event_loop()
    fut = loop.create_future()
    h = fut._loop.call_later(t, 
                        asyncio.futures._set_result_unless_cancelled, 
                        fut, None)
    try:
        return (yield from fut)
    finally:
        pass
        h.cancel()

async def worker(n):
    print(f"worker {n} start")
    # asyncio.sleep(random.randint(1, 3))
    my_sleep(1)
    print(f"worker {n} finished")
   
async def runner():
    for i in range(5):
        await worker(i)

async def main():
    await runner()
    print("exit")

if __name__ == "__main__":
    # worker(1)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())