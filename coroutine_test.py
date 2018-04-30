import asyncio

async def f(n):
    await asyncio.sleep(1)
    print("f done")

async def coro():
    print("start coro")
    await f(2)
    print("coro done")

loop = asyncio.get_event_loop()
# cor = coro()

def step(e=None):
    try:
        if e is None:
            print("send")
            result = cor.send(None)
        else:
            cor.throw(e)
    except:
        raise
    else:
        blocking = getattr(result, '_asyncio_future_blocking', None)
        if result._loop != loop:
            loop.call_soon(step, Exception)
        else:
            print("call soon")
            if blocking:
                result._asyncio_future_blocking=False
                result.add_done_callback(_wakeup)
    finally:
        pass

def _wakeup(fut):
    try:
        fut.result()
        print("get result")
    except Exception as e:
        print("excption")
        fut.set_exception(e)
        
# =========================================================
def coro2():
    print("before yield")
    yield 1
    print("after yield")

if __name__ == "__main__":
    # step()
    # loop.run_forever()
    pass

# ========================================================

    co2 = coro2()
    try:
        next(co2)
        co2.send(None)
    except StopIteration:
        pass

# =========================================================
    co = coro()
    co2 = coro()
    task = loop.create_task(co)
    task2 = loop.create_task(co2)
    loop.run_until_complete(asyncio.gather(
        task, task2
    ))