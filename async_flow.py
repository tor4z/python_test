import asyncio
import time


async def worker(n):
    """
    Some work take time
    """
    print("Worker start.")
    await asyncio.sleep(n)
    print("Worker done.")

async def main(n):
    await worker(n)
    print("Other work")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    start = time.time()
    loop.run_until_complete(
        asyncio.gather(
            main(1), main(2), main(3), main(1)))

    print(f"Took {round(time.time()-start, 3)} Sec.")