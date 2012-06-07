#!/usr/bin/env python3
"""Determine an integer d < 1000 such that 1/d will produce the longest digit
recurring cycle

Example
1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)

7 has the 7 digit recurring cycle."""
from math import log10
import num_theory
from itertools import count


def main():
    longest_recur = 1
    recur_length = 1
    potent = []
    for i in range(1, 1000):
        denom = 9
        length = 0
        last_remainder = denom % i
        if any(map(lambda x: i % x == 0, potent)):
            continue
        while True:
            denom = 10 * denom + 9
            remainder = denom % i
            if last_remainder == remainder or remainder == 0:
                if remainder != 0:
                    potent.append(i)
                break
            last_remainder = remainder
            length += 1
        if length > recur_length:
            longest_recur = i
            recur_length = length

    print(longest_recur)


def main2():
    max_num = 1000
    primes = num_theory.sieve_of_eratosthenes(max_num)
    d = 0
    max_len = 0
    for i in primes:
        denom = 10
        last_remain = 0
        for power in count(1):
            remain = denom % i
            denom *= 10
            if remain == 1:
                if power > max_len:
                    max_len = power
                    d = i
                break
            elif remain == last_remain:
                print(i, 0)
                break
            last_remain = remain
    print(d)


def main3():
    max_num = 1000
    d = 0
    max_len = 0
    for i in num_theory.sieve_of_eratosthenes(max_num):
        rest = 1
        start = set()
        for j in range(1, i):
            rest = (rest * 10) % i
            if rest in start:
                break
            start.add(rest)

        if j > max_len:
            max_len = j
            d = i
    print(d)


if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main3')
    print('time =', Timer(stmt=stmt).timeit(1))
