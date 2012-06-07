#!/usr/bin/env python3
"""Find the first of the first four consecutive numbers that have four unique
prime factors."""
from utils import runner
from num_theory import is_prime


def main():
    upper = 10 ** 6
    no_of_factor = [0] * upper
    conseq_limit = 4
    conseq = 4

    for i in range(2, upper):
        if no_of_factor[i] == conseq_limit:
            conseq += 1
        else:
            conseq = 0
            if not no_of_factor[i]:
                for j in range(2 * i, upper, i):
                    no_of_factor[j] += 1
        if conseq == conseq_limit:
            print(i - conseq_limit + 1)
            break

if __name__ == '__main__':
    runner('main')
