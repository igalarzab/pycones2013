#!/usr/bin/env python3
#
# PyCON ES 2013
# ---------------------
#
# Jose Ignacio Galarza
# @igalarzab
#

import asyncio


@asyncio.coroutine
def get_url(url):
    r, w = yield from asyncio.open_connection(url, 80)

    w.write(b'GET / HTTP/1.0\r\n\r\n')
    body = yield from r.read()
    print(body)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_url('google.com'))
