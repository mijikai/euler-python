#!/usr/bin/env python3
"""Find a prime less than one million that can be written as a sum of
consecutive primes with most terms. For example, 41 can be written as 2 + 3 + 5
+ 7 + 11 + 13, which is a sum of six consecutive primes. The number 953 is a
sum of 21 consecutive primes."""
from num_theory import sieve_of_eratosthenes
from utils import runner


def consecutive_prime(upper):
    """Given an upper bound, the method return a prime that can be written as
    a sum of most consecutive primes. The first term is not necessarily 2.
    For example:
    >>> consecutive_prime(10 ** 2)
    41
    >>> consecutive_prime(10 ** 3)
    953
    """
    primes = tuple(sieve_of_eratosthenes(upper))
    primes_set = frozenset(primes)
    maxlen = 1  # number of terms
    primesum = 0  # sum of all primes beginning from 2
    maxprime = 2  # prime found that has a maximum terms
    for i, p in enumerate(primes):
        primesum += p
        length = i + 1
        consec_prime = primesum
        for q in primes:
            if consec_prime in primes_set:
                maxlen = length
                maxprime = consec_prime
                break
            if length == maxlen:
                if consec_prime > primes[-1]:
                    return maxprime
                break
            consec_prime -= q
            length -= 1


def main():
    print(consecutive_prime(10 ** 6))


if __name__ == '__main__':
    runner('main')
