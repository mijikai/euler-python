#!/usr/bin/env python3
"""Find all the primes that can be truncated from both left and right and
still produce a prime. The number 3797 is such an example because from the
left, 797, 97 and 7 are primes and from the right, 379, 37 and 3 are also
primes. The numbers 2, 3, 5 and 7 are not considered truncatable."""
from functools import lru_cache
from math import floor, log
from num_theory import sieve_of_eratosthenes
from itertools import dropwhile, count


@lru_cache(maxsize=None)
def truncate_to_right(primes, num):
    """Returns True if ``num`` can be truncated to the right"""
    if len(str(num)) == 1:
        return num in primes
    near_pow_ten = 10 ** floor(log(num, 10))
    return (num in primes and
            truncate_to_right(primes, num % near_pow_ten))


@lru_cache(maxsize=None)
def truncate_to_left(primes, num):
    """Returns True if given ``primes``, ``num`` can be truncated to the left
    and still produce a prime."""
    if len(str(num)) == 1:
        return num in primes
    return num in primes and truncate_to_left(primes, num // 10)


def truncate_to_both(primes, num):
    """Returns True if ``num`` is still a prime when truncated from both left
    and right."""
    return truncate_to_left(primes, num) and truncate_to_right(primes, num)


def truncatable_to_left_primes(primes):
    trunc_primes = []
    for i in (2, 3, 5, 7):
        trunc_primes.append(i)
        yield i
    trunc_primes_prev = trunc_primes
    trunc_primes = []

    while trunc_primes_prev:
        trunc_primes = []
        for i in trunc_primes_prev:
            for j in (1, 3, 7, 9):
                num = 10 * i + j
                if num in primes:
                    trunc_primes.append(num)
                    yield num
        trunc_primes_prev = trunc_primes


def truncatable_primes(primes):
    for j in truncatable_to_left_primes(primes):
        if truncate_to_right(primes, j):
            yield j


def main():
    upper = 10 ** 6
    primes = frozenset(sieve_of_eratosthenes(upper))
    trunc_primes = list(truncatable_primes(primes))
    for i in trunc_primes:
        print(i)
    print('Sum is {}'.format(sum(trunc_primes)))


def main2():
    for i in (truncate_to_left, truncate_to_right):
        i.cache_clear()
    upper = 10 ** 3
    primes = tuple(sieve_of_eratosthenes(upper))
    primes_set = frozenset(primes)
    trunc_primes = tuple(filter(
        lambda num: truncate_to_both(primes_set, num),
        dropwhile(lambda num: num < 10, primes)))
    for i in trunc_primes:
        print(i)
    print('Sum is {}'.format(sum(trunc_primes)))


if __name__ == '__main__':
    print(__doc__)
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
