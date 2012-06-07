#!/usr/bin/env python3
"""Count the number of unique power a ** b where 2 <= a <= 100 and
<= b <= 100"""

from itertools import product
from math import log


lower = 2  # lowest possible value of the exponents and base
higher = 100  # higest one

base = range(lower, higher + 1)
power = range(lower, higher + 1)


def power_tuple(tup):
    """Find the power from a tuple of numbers of length two. The first
    item is the base and the last is the exponent.

    Examples:
    >>> power_tuple((3, 2))
    9
    >>> power_tuple((9, 0.5))
    3.0
    """

    if len(tup) != 2:
        raise ValueError(
            'tuple must be of length 2; given {}'.format(len(tup)))

    return pow(*tup)


def count_results():
    # get all the posible combinations of base and power
    pos_combi = product(base, power)
    result = set(map(power_tuple, pos_combi))

    # get the length of the result
    return len(result)


def count_results2():
    prod = set(x ** y for x in base for y in power)
    return len(prod)


def main():
    print(count_results2())


if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
