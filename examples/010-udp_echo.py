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


class EchoServer:

    def connection_made(self, transport):
        print('Connected')
        self.transport = transport

    def datagram_received(self, data, addr):
        print('[R]', data.decode())
        self.transport.sendto(data, addr)

    def connection_refused(self, exc):
        print('Connection refused')

    def connection_lost(self, exc):
        print('Connection lost')


class EchoClient:

    def connection_made(self, transport):
        self.transport = transport
        self.transport.sendto(b'Hola caracola')
        print('[S] ', 'Hola caracola')

    def datagram_received(self, data, addr):
        print('[R] ', data.decode())

    def connection_refused(self, exc):
        print('Connection refused:', exc)

    def connection_lost(self, exc):
        print('Connection lost', exc)
        asyncio.get_event_loop().stop()


def start_server(event_loop):
    t = asyncio.Task(event_loop.create_datagram_endpoint(
        EchoServer, local_addr=('127.0.0.1', 8080)))
    event_loop.run_until_complete(t)


def start_client(event_loop):
    t = asyncio.Task(event_loop.create_datagram_endpoint(
        EchoClient, remote_addr=('127.0.0.1', 8080)))
    event_loop.run_until_complete(t)


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
