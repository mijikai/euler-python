#!/usr/bin/env python3
"""If one example of an arithmetic sequence of primes that is a permutation of
each other is 1487, 4817, 8147, find the other and its 12 digit
concatenation."""
from num_theory import sieve_of_eratosthenes
from itertools import permutations, dropwhile
from functools import reduce
from utils import runner


def main():
    lower, upper = 10 ** 3, 10 ** 4
    primes = tuple(dropwhile(lambda prime: prime < lower,
            sieve_of_eratosthenes(upper)))
    no_of_terms = 3
    for prime in primes:
        differences = {}
        for perm in permutations(map(int, str(prime))):
            other = reduce(lambda a, b: 10 * a + b, perm, 0)
            diff = other - prime
            if other in primes and diff > 0:
                differences.setdefault(diff, {prime}).add(other)
                differences.setdefault(2 * diff, {prime}).add(other)
        for diff in filter(lambda d: len(differences[d]) == no_of_terms, differences):
            print(diff, differences[diff], ''.join(map(str, differences[diff])))


if __name__ == '__main__':
    runner('main')
