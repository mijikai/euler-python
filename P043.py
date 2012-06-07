#!/usr/bin/env python3
"""Find the sum of 0 to 9 pandigital numbers that has the property
    d2d3d4 % 2 == 0
    d3d4d5 % 3 == 0
    d4d5d6 % 5 == 0
    d5d6d7 % 7 == 0
    d6d7d8 % 11 == 0
    d7d8d9 % 13 == 0
    d8d9d10 % 17 == 0
where
    d1d2d3d4d5d6d7d8d9d10 is a 10 digit number. 
One example of such number is 1406357289.
"""
from functools import reduce
from utils import runner


def substring_recur(first, digits, divisors):
    """Returns a generator of a list of digits that has the substring
    divisibility given the front digit ``first``, the ``digits`` to be use and
    the ``divisors``."""
    assert len(digits) == len(divisors)
    if len(divisors) == 0:
        yield [first % 10]

    for num in filter(lambda elem: not elem % divisors[0],
            map(lambda elem: 10 * (first % 100) + elem, digits)):
        last = first % 10
        i = num % 10
        remaining = tuple(j for j in digits if j != i)
        for j in substring_recur(num, remaining, divisors[1:]):
            j.insert(0, last)
            yield j


def substring_iter(first, digits, divisors):
    assert len(digits) == len(divisors)
    digits = tuple(digits)

    stack = [(first, digits, divisors, [first])]
    
    while stack:
        first, digits, divisors, previous = stack.pop()
        if len(digits) == 0:
            yield res
            continue

        for num in filter(lambda elem: not elem % divisors[0],
                map(lambda elem: 10 * (first % 100) + elem, digits)):
            i = num % 10
            remaining = tuple(j for j in digits if j != i)
            res = list(previous)
            res.append(i)
            stack.insert(0, (num, remaining, divisors[1:], res))
substring_iter.__doc__ = substring_recur.__doc__


def main():
    pandigitals = []
    divisors = (1, 1, 2, 3, 5, 7, 11, 13, 17)
    for i in range(1, 10):
        digits = tuple(j for j in range(10) if i != j)
        pandigitals.extend(substring_recur(i, digits, divisors))

    pandigitals = tuple(map(lambda lst: reduce(lambda a, b: 10 * a + b,
        lst, 0), pandigitals))
    for i in pandigitals:
        print(i)
    print('The sum is {}'.format(sum(pandigitals)))


runner('main')
