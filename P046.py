#!/usr/bin/env python3
"""Find the smallest odd composite number which cannot be written as a sum of
a prime and twice a square. The number 9 fails because it can be represented as
7 + 2 * 1 ** 2"""
from utils import runner
from num_theory import sieve_of_eratosthenes, is_prime
from itertools import filterfalse, count
from math import sqrt, floor


def main():
    for i in filterfalse(is_prime, count(9, 2)):
        found = True
        for j in sieve_of_eratosthenes(i):
            num = (i - j) // 2
            if floor(sqrt(num)) ** 2 == num:
                found = False
                break
        if found:
            print(i)
            break


if __name__ == '__main__':
    runner('main')
