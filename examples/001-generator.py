#!/usr/bin/env python3
#
# PyCON ES 2013
# ---------------------
#
# Jose Ignacio Galarza
# @igalarzab
#


def work_hard_normal():
    results = []

    for i in range(1, 10):
        print('Working very hard %d times...' % i)
        results.append(i)

    return results


def working_hard_generator():
    for i in range(1, 10):
        print('Working very hard %d times...' % i)
        yield i


if __name__ == '__main__':

    # Without a generator
    for result in work_hard_normal():
        if result % 5 == 0:
            print('Eureka!')
            break

    # With a generator
    for result in working_hard_generator():
        if result % 5 == 0:
            print('Eureka!')
            break
