#!/usr/bin/env python3
"""What is the largest n-digit number that is composed of numbers from 1 to n
that is a prime?"""
from functools import reduce
from itertools import takewhile


def main():
    maximum = 0
    for i in range(1, 8):         
        front_digits = tuple(takewhile(lambda elem: elem <= i, range(1, 10)))
        last_digits = tuple(takewhile(lambda elem: elem <= i, [1, 3, 7, 9]))
        for front in permutations(front_digits, i - 1):
            for last in last_digits:
                if last not in front:
                    digits = front + (last,)
                    num = reduce(lambda a, b: 10 * a + b, digits, 0)
                    if is_prime(num):
                        maximum = num
    print(maximum)

    
if __name__ == '__main__':
    print(__doc__)
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
