#!/usr/bin/env python3
#
# PyCON ES 2013
# ---------------------
#
# Jose Ignacio Galarza
# @igalarzab
#


class TreeBasic:

    def __init__(self, data, left=None, right=None):
        self.left = left
        self.data = data
        self.right = right

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node

        yield self.data

        if self.right:
            for node in self.right:
                yield node


class TreeYieldFrom:

    def __init__(self, data, left=None, right=None):
        self.left = left
        self.data = data
        self.right = right

    def __iter__(self):
        if self.left:
            yield from self.left

        yield self.data

        if self.right:
            yield from self.right

if __name__ == '__main__':
    node1, node2 = TreeBasic(1), TreeBasic(2)
    node3 = TreeBasic(3, node1, node2)

    for data in node3:
        print(data)

    node4, node5 = TreeYieldFrom(1), TreeYieldFrom(2)
    node6 = TreeYieldFrom(3, node1, node2)

    for data in node6:
        print(data)
