#!/usr/bin/env python3
"""Given n ^2 + bn + c, this module computes the product of b and c such that
|b|, |c| < 1000 and the equation will produce the maximum consecutive number of
primes starting from n = 0."""
from fractions import Fraction
from itertools import count
from num_theory import sieve_of_eratosthenes, sieve_of_eratosthenes_bool


class QuadradicEquation(object):
    """Create an object that evaluates a * x ^ 2 + b * x + c when called."""
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def __call__(self, n):
        return self.a * n ** 2 + self.b * n + self.c

    def __eq__(self, other):
        if type(other) == type(self):
            if (self.a, self.b, self.c) == (other.a, other.b, other.c):
                return True
        return False

    def __repr__(self):
        return '{}({}, {}, {})'.format(self.__class__.__name__,
                self.a, self.b, self.c)


def main():
    """Search for the pair |b| and |c| < 1000 where the maximum consecutive
    number of primes is produced for n, starting with n = 0."""
    limit = 1000
    max_primes = 0
    max_b, max_c = 0, 0
    is_prime = sieve_of_eratosthenes_bool(limit * 100)
    primes = sieve_of_eratosthenes(limit)
    for c in primes:
        for b in range(-c, limit, 2):
            for n in count(1):
                res = n * n + b * n + c
                if res < 1 or not is_prime[res]:
                    if max_primes < n:
                        max_primes = n
                        max_b, max_c = b, c
                        print(max_primes, max_b, max_c, end='\n')
                    break
    print(max_b, max_c, max_b * max_c)


if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
