#!/usr/bin/env python3
#
# PyCON ES 2013
# ---------------------
#
# Jose Ignacio Galarza
# @igalarzab
#

import os
from helpers import coroutine


def list_dir(path, target):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            target.send(filename)

@coroutine
def filter_str(pattern, target):
    while True:
        filename = (yield)
        if pattern in filename:
            target.send(filename)


@coroutine
def print_match():
    while True:
        result = (yield)
        print(result)


if __name__ == '__main__':
    list_dir('.', filter_str('py', print_match()))
