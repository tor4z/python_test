import random
import asyncio
from asyncio.futures import Future
import time

def worker(n):
    print(f"worker {n} start")
    asyncio.sleep(random.randint(1, 3))
    print(f"worker {n} finished")
    #fut.set_result(None)
   
def runner():
    futs = [] 
    for i in range(5):
        fut = Future()
        futs.append(fut)
        worker(i, fut)
    return futs

async def main():
    futs = runner()
    for fut in futs:
        await fut
    print("exit")

if __name__ == "__main__":
    main()
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())