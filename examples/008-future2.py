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
def wait_and_resolve(future):
    for i in range(3):
        print('Sleeping 1 second')
        yield from asyncio.sleep(1)

    # Try both!
    future.set_result('Future is done!')
    # future.set_exception(Exception)


@asyncio.coroutine
def wait_for_future(future):
    try:
        yield from future
    except Exception:
        print('Future is sad :(')
    else:
        print('Future is happy :D')

    asyncio.get_event_loop().stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.Future()

    asyncio.Task(wait_and_resolve(future))
    asyncio.Task(wait_for_future(future))

    loop.run_forever()
    print('loop stopped')
