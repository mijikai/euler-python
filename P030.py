#!/usr/bin/env python3
"""Find the sum of all numbers that can be written as the sum of the fifth
power of their digits."""
from itertools import combinations_with_replacement, chain
from math import ceil, log
from functools import partial


def num_to_digit(num):
    """Make an iterator of digits of num. The argument must be a whole number."""
    return iter(map(int, str(num)))


def is_narcissist(num, expo):
    """"Determine whether ``num`` is a narcissist given ``expo``. A number is
    narcissist such that the sum of the ``expo`` power of the ``num``'s digit
    is the ``num`` itself."""
    return num == sum(map(lambda digit: digit ** expo, num_to_digit(num)))


def power_order(iterable, limit=None):
    """Compute like powerset but allow repetition to occur.
    For example:
    >>> power_order([1, 2])
    [(), (1,), (2,), (1, 1), (1, 2), (2, 2)]
    """
    lst = list(iterable)
    if limit == None:
        limit = len(lst)
    return chain.from_iterable(combinations_with_replacement(lst, r)
            for r in range(limit + 1))


def digit_combinations(max_length):
    """Build an iterable composed of the combinations of digit of length one to
    max_length. Each element is a tuple"""

    def is_not_start_zero(tup):
        """Determine whether tuple does not starts with zero. If tuple is of
        length one, returns true."""
        return not (tup and tup[0] == 0 and len(tup) != 1)

    combi = power_order(range(10), max_length)
    next(combi)  # remove the empty tuple
    return filter(is_not_start_zero, combi)


def sum_pow_digit(iterable, expo):
    """Find out the sum of the expo power of the elements of iterable."""
    return sum(digit ** expo for digit in iterable)


def sum_narcissist():
    expo = 5
    max_digit_length = ceil(log(9 ** expo, 10)) + 1
    res = sum(filter(partial(is_narcissist, expo=expo),
            (sum_pow_digit(iterable, expo)
                for iterable in digit_combinations(max_digit_length))))
    return res - 1


def one_liner():
    return sum(filter(lambda num: num == sum(map(lambda digit: digit ** 5,
        (int(digit) for digit in str(num)))), range(int(10e2), int(10e5))))


def main():
    expo = 5
    lower = int(10e2)
    upper = int(10e5)
    print(__doc__)
    # print(one_liner())
    # print(sum(filter(lambda num: is_narcissist(num, expo),
    #         range(lower, upper))))
    print(sum_narcissist())


if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
