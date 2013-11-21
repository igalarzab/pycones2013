#!/usr/bin/env python3
#
# PyCON ES 2013
# ---------------------
#
# Jose Ignacio Galarza
# @igalarzab
#

import asyncio
import sys

try:
    import signal
except ImportError:
    signal = None


class EchoServer(asyncio.Protocol):

    def connection_made(self, transport):
        print('Connected')
        self.transport = transport

    def data_received(self, data):
        print('[R] ', data.decode())
        print('[S] ', data.decode())
        self.transport.write(data)

    def eof_received(self):
        pass

    def connection_lost(self, exc):
        print('Connection lost')


class EchoClient(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        self.transport.write(b'Hola caracola')
        print('[S] ', 'Hola caracola')

    def data_received(self, data):
        print('[R] ', data)

    def eof_received(self):
        pass

    def connection_lost(self, exc):
        print('Connection lost')
        asyncio.get_event_loop().stop()


def start_client(event_loop):
    task = asyncio.Task(event_loop.create_connection(EchoClient, '127.0.0.1', 8080))
    event_loop.run_until_complete(task)


def start_server(event_loop):
    server = event_loop.create_server(EchoServer, '127.0.0.1', 8080)
    event_loop.run_until_complete(server)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Call me with --server or --client flag')
        sys.exit()

    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, loop.stop)

    if sys.argv[1] == '--server':
        start_server(loop)
    else:
        start_client(loop)

    loop.run_forever()
