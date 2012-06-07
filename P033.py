#!/usr/bin/env python3
"""Find the product of all fraction less than one containing two digits in the
numerator and denominator in which a correct result can be obtain by cancelling
some digit in the numerator and denominator.
One example of such fraction is
    49   4
    -- = -
    98   9
which is obtained by cancelling 9.
"""
from math import floor
from fractions import Fraction
from operator import mul
from functools import reduce


def cancelled_digit(two_digit):
    """Given a two digit number, find y such that
        x y   x
        --- = -
        y z   z
    Example:
    >>> cancelled_digit(48) # 49 / 98 == 4 / 8
    9.0
    """
    tens, ones = two_digit // 10, two_digit % 10
    return 9 * tens * ones / (10 * tens - ones)


def is_digit(num):
    """Returns True if num is an int less than 10 but greater than 0."""
    return 0 < num < 10 and num - floor(num) == 0


def make_curious_frac(num):
    """Return a Fraction so that
        x y   x
        --- = -
        y z   z
    Example:
    >>> make_curious_frac(48)  # 49 / 98 == 4 / 8
    Fraction(1, 2)
    """
    digit = int(cancelled_digit(num))
    numer = 10 * (num // 10) + digit
    denom = 10 * digit + num % 10
    return Fraction(numer, denom)


def main():
    curious_frac_seq = map(make_curious_frac,
        filter(lambda num: bool(is_digit(cancelled_digit(num)) and
                num % 11 != 0),
            range(10, 100)))
    print(__doc__)
    print(reduce(mul, curious_frac_seq, 1))


if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
