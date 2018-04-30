import asyncio
import random

async def worker(loop, n):
    print(f"worker {n} start.")
    await asyncio.sleep(random.randint(1, 3))
    print(f"worker {n} done.")
    # loop.stop()

async def main(loop):
    for i in range(5):
        loop.create_task(worker(loop, i))
    
    #loop.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()