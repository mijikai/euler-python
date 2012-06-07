#!/usr/bin/env python3
"""Computes the value of n where log(F(n), 10) == 1000 holds.
F is the fibonacci function."""
from math import log, ceil, sqrt


def main():
    sqrt_five = sqrt(5)
    golden_ratio = (1 + sqrt_five) / 2
    #  n(F) = floor(log(F * sqrt(5) + 1/2, golden_ratio))
    print(ceil(999 * log(10, golden_ratio) +
        log(sqrt_five, golden_ratio)))


if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
