#!/usr/bin/env python3
"""Find two numbers m, n such that m, n, m + n, m - n are pentagonal numbers.
The number m - n must be the smallest among all possibilities.
Pentagonal numbers satisfy the following property:
    P(i) = n * (3 * i - 1) / 2
"""
from math import sqrt, floor
from itertools import count


def is_pentagonal(num):
    """Returns true if num is pentagonal, otherwise False."""
    discriminant = 1 + 24 * num
    sqrt_disc = floor(sqrt(discriminant))
    return sqrt_disc ** 2 == discriminant and (1 + sqrt_disc) % 6 == 0


def pentagonal(n):
    """Returns the nth pentagonal number."""
    return n * (3 * n - 1) // 2


def main():
    table = {}
    found = False
    for i in count(1):
        pen1 = pentagonal(i)
        table[i] = pen1
        for j in range(i - 1, 0, -1):
            pen2 = table[j]
            if is_pentagonal(pen1 - pen2) and is_pentagonal(pen1 + pen2):
                print('{} - {} = {}'.format(pen1, pen2, pen1 - pen2))
                found = True
                break
            print(pen1, pen2, end='\r')
        if found:
            break


if __name__ == '__main__':
    print(__doc__)
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
