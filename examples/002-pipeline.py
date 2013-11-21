#!/usr/bin/env python3
#
# PyCON ES 2013
# ---------------------
#
# Jose Ignacio Galarza
# @igalarzab
#


def gen_sentence():
    for sentence in ['ola', 'ke', 'ase!']:
        yield sentence


def kaninizaitor(words):
    for word in words:
        yield word.upper()


if __name__ == '__main__':
    for result in kaninizaitor(gen_sentence()):
        print(result, end=' ')

    print()
