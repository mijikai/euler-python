#!/usr/bin/env python3
"""Calulates the sum of the spiral.
The 5 x 5 side

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

has a spiral passing through 1 3 5 7 9 13 17 21 25 and has the sum of 101.
"""
from polynomial import Polynomial
from fractions import Fraction
from math import sqrt


sum_linear = Polynomial([0, Fraction(1, 2), Fraction(1, 2)])
sum_quad = Polynomial([0, Fraction(1, 6), Fraction(1, 2), Fraction(1, 3)])
sum_const = Polynomial([0, 1])

def sum_spiral(sides):
    """
    >>> sum_spiral(1)
    Fraction(1, 1)
    >>> sum_spiral(3)
    Fraction(25, 1)
    >>> sum_spiral(5)
    Fraction(101, 1)
    """
    n = (sides - 1) // 2
    return 4 * (4 * sum_quad(n) + sum_linear(n) + sum_const(n)) + 1


def _test():
    import doctest
    doctest.testmod()


def main():
    sides = 1001
    print(sum_spiral(sides))


if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
