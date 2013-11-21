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
def wait_and_resolve_future(future):
    for i in range(3):
        print('Sleeping 1 second')
        yield from asyncio.sleep(1)

    future.set_result('Future is done!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    future = asyncio.Future()
    asyncio.Task(wait_and_resolve_future(future))

    loop.run_until_complete(future)
    print(future.result())
