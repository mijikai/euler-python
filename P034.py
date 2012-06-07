#!/usr/bin/env python
"""Find the sum of all numbers which are equal to the sum of the factorial of
their digits."""
from utils import digitsof, power_comb_with_repetition
from functools import reduce
from operator import mul
from itertools import takewhile


def factorial(integer):
    return reduce(mul, range(1, integer + 1), 1)


def main():
    digits_factorial = tuple(factorial(i) for i in range(10))
    no_of_digits = len(str(9 * digits_factorial[9]))
    numbers = takewhile(lambda tup: len(tup) <= no_of_digits,
            power_comb_with_repetition(range(10)))
    candidates = map(
        lambda num: (tuple(digitsof(sum(digits_factorial[digit]
            for digit in num))), num),
        numbers)

    summand = map(lambda num: sum(digits_factorial[digit] for digit in num[0]),
        filter(lambda tup: sorted(tup[0]) == sorted(tup[1]), candidates))
    summand = list(summand)[2:]
    for i in summand:
        print(i)
    print(sum(summand))


def one_liner():
    digits_factorial = tuple(factorial(i) for i in range(10))
    return list(filter(lambda num: sorted(digitsof(sum(digits_factorial[digit]
            for digit in num))) == sorted(num),
        power_comb_with_repetition(range(6))))


if __name__ == '__main__':
    print(__doc__)
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
