#!/usr/bin/env python3
"""Find the largest 1-9 pandigital number that can be form as the concatination
of the products of a and (1, 2, ..., n) where a > 0 and n > 1.
Example:
    918273645 is the concatination of products 9 * 1, 9 * 2, 9 * 3, 9 * 4 and
    9 * 5 (a = 9; n = {1, 2, 3, 4, 5})
"""
from math import log, floor


def have_unique_nonzero_digits(integer):
    """Returns True if each digit in integer is unique and nonzero, otherwise
    False.
    Example:
    >>> have_unique_nonzero_digits(123)
    True
    >>> have_unique_nonzero_digits(102)
    False
    >>> have_unique_nonzero_digits(232)
    False
    """
    digits = tuple(map(int, str(integer)))
    return 0 not in digits and len(set(digits)) == len(digits)


def largest_pandigital():
    """Return the largest 1 to 9 pandigital number that can be form by
    concatinating the products of a and n = {1, 2, .., n}"""
    maxnum = 0
    found = False
    for i in filter(have_unique_nonzero_digits, range(10 ** 5, 1, -1)):
        num = i
        for j in range(2 ,10):
            other = i * j
            exp = floor(log(other, 10)) + 1
            num = num * 10 ** exp + other

            if have_unique_nonzero_digits(num):
                if floor(log(num, 10)) + 1 == 9:
                    return num
            else:
                break


def main():
    print(largest_pandigital())


if __name__ == '__main__':
    print(__doc__)
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
