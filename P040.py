#!/usr/bin/env python3
"""Given the sequence
    123456789101112131415
where
    a(1) = 1
    a(12) = 1
    a(15) = 2
find the value of 
     7
    PI  a(10 ** (i - 1))
    i=1
"""
from functools import reduce
from itertools import count


def subindex(index):
    """Return a tuple of the number of digits and its offset. For example, if
    index is 12, the current number in the sequence 1, 2, 3, ..., 1, 1, 1, 2 is
    11. The number of digits is 2 and the offset is 1, beginning from 10."""
    assert index > 0
    sub = index
    diff = 0
    for digit_count in count(1):
        diff = 9 * digit_count * 10 ** (digit_count - 1)
        if diff > sub:
            return (digit_count, sub)
        else:
            sub -= diff


def subindex2(index):
    # Find the summation of 1 * 10, 2 * 10, 3 * 10, ...
    # The sum is composed by the number 987654320 that repeat itself every
    # 9 digit exept for the beginning and the end.
    front = (ind - 1) // 9
    expo = (ind - 1) % 9 + 1
    base = 987654320
    num = front * 10 ** expo + base % (10 ** expo)
    return reduce(lambda a, b: a * 10 ** 9 + base, range(front), num) + 1


def sequence(index):
    """Return the ``index``th number of the sequence 1, 2, ..., 1, 1, 1, 2, 1,
    3, ... """
    digit_count, sub = subindex(index)
    number = (sub - 1) // digit_count + 10 ** (digit_count - 1)
    return number // 10 ** ((digit_count - sub) % digit_count) % 10


def main():
    limit = 7
    seq = tuple(map(sequence, map(lambda expo: 10 ** expo, range(0, limit))))
    print('The digits are {}'.format(seq))
    print('The product is {}'.format(reduce(mul, seq, 1)))


if __name__ == '__main__':
    print(__doc__)
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
