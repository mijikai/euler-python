#!/usr/bin/env python3
"""Calculates the sum of the even Fibonacci terms less than 4e6"""
from math import ceil, floor, sqrt, log


def fibo(n):
    """Calculates the nth Fibonacci sequence starting with F(0) = 0 and
    F(1) = 1."""
    golden_ratio = (1 + sqrt(5)) / 2
    return round(golden_ratio ** n / sqrt(5))


def nth_fibo(f):
    """Returns n which satisfy the following relation f = fibo(n)."""
    golden_ratio = (1 + sqrt(5)) / 2
    return floor(log(f * sqrt(5) + 0.5, golden_ratio))


def main():
    print(__doc__)
    print(sum(map(fibo, range(0, nth_fibo(4e6) + 1, 3))))


if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
