#!/usr/bin/env python3
"""Find the sum of all products whose multiplicand/multiplier/produce identity
can be written as a 1 through 9 pandigital
Example is 39 * 186  = 7254"""
from subprocess import check_output
from itertools import permutations, dropwhile, combinations, chain
from functools import reduce
from operator import mul, or_
from math import sqrt, ceil
from utils import powerset, unique_n_digits, digits_int


def factor(integer):
    """Generate the prime factors of integer. If a prime p divides ``integer``
    n times, it will be included n times."""
    return map(int, check_output(['factor', str(integer)]).decode().split()[1:])


def drop_parallel(seq, parallel):
    """Drop the first elements in seq that match in parallel.
    For example:
    >>> list(drop_parallel([1, 2, 3], [2, 3]))
    [1]
    >>> list(drop_parallel([1, 2, 2, 3, 2], [2]))
    [1, 2, 3, 2]
    >>> list(drop_parallel([1, 2, 3, 4], [3, 2, 1]))
    [1, 2, 4]
    """
    
    seq = iter(seq)
    for i in parallel:
        elem = next(seq)
        while i != elem:
            yield elem
            elem = next(seq)
    for elem in seq:
         yield elem


def partition(iterable, num=1):
    seq = tuple(iterable)
    if num <= 1:
        yield [seq]
        raise StopIteration
    if not seq:
        yield [()] * num
        raise StopIteration

    for head in powerset(seq[:len(seq) - 1]):
        tail = drop_parallel(seq, head)
        for lst in partition(tail, num - 1):
            lst.insert(0, head)
            yield lst


def main():
    digit_len = 4
    digits = range(1, 10)
    zero_set = set([0])
    pandigital = []
    for num in unique_n_digits(digits, digit_len):
        digits_of_num = set(digitsof(num))
        for a in range(1, ceil(sqrt(num))):
            if num % a != 0:
                continue

            b = num // a
            terms_set = (set(digitsof(t)) for t in [a, b])
            expr = chain(terms_set, (digits_of_num,))
            if len(reduce(or_, expr, zero_set)) == 10:
                print(num)
                pandigital.append(num)
                break
    print('Sum is', sum(pandigital))


def main2():
    digit_len = 4
    digits = range(1, 10)
    zero_set = set([0])
    pandigital = []
    for num in unique_n_digits(digits, digit_len):
        digits_of_num = set(digitsof(num))
        for terms in partition(factor(num), 2):
            terms = tuple(reduce(mul, t, 1) for t in terms)
            terms_set = tuple(set(digitsof(t)) for t in terms)
            expr = tuple(chain(terms_set, (digits_of_num,)))
            if len(reduce(or_, expr, zero_set)) == 10:
                print(num)
                pandigital.append(num)
                break
    print('Sum is', sum(pandigital))


def one_liner():
    pandigital = []
    for i in filter(
        lambda integer: any(
            map(
                lambda mulp: len(
                    reduce(
                        lambda a, b: (set(a) | set(digitsof(b))),
                        chain(map(lambda y: reduce(mul, y, 1), mulp),
                            [integer]), [0])) == 10,
                        partition(factor(integer), 2))),
            unique_n_digits(range(1,10),4)):
        print(i)
        pandigital.append(i)
    print('Sum is', sum(pandigital))


if __name__ == '__main__':
    print(__doc__)
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
