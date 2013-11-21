#!/usr/bin/env python3
#
# PyCON ES 2013
# ---------------------
#
# Jose Ignacio Galarza
# @igalarzab
#

import os


def coroutine(func):
    """
    Decorator to auto-start coroutines.
    Got it from: PEP-0342
    """

    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    wrapper.__name__ = func.__name__
    wrapper.__dict__ = func.__dict__
    wrapper.__doc__  = func.__doc__
    return wrapper


def list_dir(directory):
    for item in os.listdir(directory):
        yield item


def echo_text(number_times):
    for i in range(number_times):
        yield 'Hi dude!'
