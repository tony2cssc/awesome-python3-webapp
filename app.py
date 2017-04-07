'''
This is a simple application built on the top of aiohttp.
'''

import logging
import asyncio
from datetime import datetime
from aiohttp import web



logging.basicConfig(level=logging.INFO)

def index(request):
    '''
    It generates index page
    '''
    return web.Response(content_type='text/html', body=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    '''
    Initialize the application
    '''
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()