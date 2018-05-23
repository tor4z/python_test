from aiohttp import web


WS_FILE = "index.html"


async def ws_handler(request):
    resp = web.WebSocketResponse()
    available = resp.can_prepare(request)
    if not available:
        with open(WS_FILE, 'rb') as fp:
            return web.Response(body=fp.read(), content_type='text/html')

    await resp.prepare(request)

    await resp.send_str('Welcome!!!')

    try:
        async for msg in resp:
            if msg.type == web.WSMsgType.TEXT:
                await resp.send_str(msg.data)
            else:
                return resp
        return resp

    finally:
        print('disconnected.')
        await resp.send_str('disconnected.')



if __name__ == "__main__":
    app = web.Application()
    app.router.add_get("/", ws_handler)
    web.run_app(app, port=9000)