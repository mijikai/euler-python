#!/usr/bin/env python3
"""Computes the sum of multiples of 3 or 5 below 1000"""
from math import floor


def arithmetic_nth_term(term, start, diff):
    """
    Determine what is n to make the equation
        term = start + (n - 1) * diff
    will be an integer ``n`` that satisfies
        a < term < b
        a = start + (n - 1) * diff
        b = start + n * diff
    """
    return floor((term - start) / diff) + 1


def arithmetic_sum(start, n, diff):
    """
    Calculate the sum of the arithmetic sequence ``start + (n - 1) * diff``
    from 1 to n.
    """
    return n * (2 * start + (n - 1) * diff) / 2


def main():
    # Make 15 negative so that the redundant from the sum of the multiples of
    # 3 and 5 is subtracted
    base = (3, 5, -15)
    limit = 1e3 - 1
    print(__doc__)
    print(sum(map(lambda init: arithmetic_sum(init,
        arithmetic_nth_term(limit, init, init), init), base)))


if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
