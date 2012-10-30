#!/usr/bin/env python3
"""Find the sum of a five item set of primes in which picking any two elements
and concatenating them in any order will produce another prime. The sum must be
the minimum of all possible combinations."""
from itertools import count
from functools import lru_cache
from math import log10
from num_theory import is_prime
from utils import runner


def generate_primes(start=1):
    """Generate an iterable of primes greater than `start`."""
    return (i for i in count(start) if is_prime(i))


def prime_concat(length, upper_bound=None):
    """Return a set of primes in which picking any two elements and
    concatenating them in any order would result to a prime number. The
    `length` is the size of the set to be generateed. If `upper_bound` is not
    None, the elements in the set will be less than that argument."""
    return prime_concat_helper((), generate_primes(3), length, upper_bound)


@lru_cache(None)
def is_prime_concat(a, b):
    """Returns True if the concatenation of the numbers `a` and `b` in any
    order is a prime, otherwise False"""
    left_concat = 10 ** int(log10(a) + 1) * b + a
    right_concat = 10 ** int(log10(b) + 1) * a + b
    return is_prime(left_concat) and is_prime(right_concat)


def prime_concat_helper(primes, list_primes, length, upper_bound=None):
    """A helper function for `primes_concat`. The argument `primes` is the
    currently generated primes, `list_primes` is an iterable of
    `prime_numbers`, `length` is the number of primes left, and `upper_bound`
    is the limit for which primes that will be pick up is less than that
    number. If there are no possible primes that fit with the constraint, None
    is returned."""
    if length < 1:
        return primes

    if not primes:
        while True:
            current = next(list_primes)
            if upper_bound is not None and current > upper_bound:
                return None

            ret = prime_concat_helper(primes + (current,),
                    generate_primes(current + 1), length - 1, upper_bound)
            if ret is not None:
                return ret

    while True:
        current = next(list_primes)
        if upper_bound is not None and current > upper_bound:
            return None

        for i in primes:
            if not is_prime_concat(i, current):
                break
        else:
            ret = prime_concat_helper(primes + (current,),
                    generate_primes(current + 1), length - 1, upper_bound)
            if ret is not None:
                return ret


def main():
    num_primes = 5
    upper_bound = 10 ** 4
    print(sum(prime_concat(num_primes, upper_bound)))


if __name__ == '__main__':
    runner('main')

