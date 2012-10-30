#!/usr/bin/env python3
from itertools import count
from utils import runner
from num_theory import is_prime


def sum_formula(first_term, diff, offset=0):
    return (lambda n: n * (2 * first_term + (n - 1) * diff) / 2 + offset)


def main():
    upper_right = sum_formula(2, 8, 1)
    upper_left = sum_formula(4, 8, 1)
    lower_left = sum_formula(6, 8, 1)

    number_of_primes = 0
    numbers_in_diag = 1
    for i in count(1):
        numbers_in_diag += 4
        for func in (upper_right, upper_left, lower_left):
            if is_prime(int(func(i))):
                number_of_primes += 1
        if number_of_primes / numbers_in_diag * 100 < 10:
            print(number_of_primes, numbers_in_diag, i * 2 + 1)
            break


if __name__ == '__main__':
    runner('main')

