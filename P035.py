#!/usr/bin/env python3
"""A circular prime is a number such that all rotations of its digits is a
prime. For example, 197 is a circular prime because 719 and 917 are also
primes.

Find the number of cicular primes below one million."""
from utils import power_comb_with_repetition, is_prime, towhole


def no_of_circular_primes(digits):
    """Determine the number of unique primes that are circular out of
    ``digits``.
    For example:
    >>> no_of_circular_primes([1,7,9])  # 197, 719, 917 are circular primes
    3
    >>> no_of_circular_primes([1])  # 1 is not a prime
    0
    >>> no_of_circular_primes([1, 1])  # 11 is a circular prime equal to its rotation
    1
    """
    primes = set()
    for i in unique_rotate(digits):
        seq = list(i)
        rotations = set()
        for j in range(len(seq)):
            num = towhole(seq)
            if is_prime(num):
                rotations.add(num)
                item = seq.pop()
                seq.insert(0, item)
            else:
                rotations.clear()
                break
        primes.update(rotations)
    return len(primes)


def main():
    # ignore even numbers and 5 because after some rotation,
    # a composite will be generated
    digits = [1, 3, 7, 9]
    limit = 6  # generate up to six digit number

    number_circ = sum(map(no_of_circular_primes,
        power_comb_with_repetition(digits, limit)))
    number_circ += 2  # 2 and 3 is a circular prime not caught by previous
    print(number_circ)


if __name__ == '__main__':
    print(__doc__)
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
