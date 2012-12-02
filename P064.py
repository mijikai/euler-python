#!/usr/bin/env python3
"""Find the number of continued fraction expansion of
square roots <= 10000 that has odd number of repeating
blocks"""
from math import sqrt, floor
from fractions import Fraction


def get_continued_sqrt(num):
    m, d, a0 = 0, 1, floor(sqrt(num))
    a = a0

    m = d * a - m
    d = (num - m ** 2) // d
    if d == 0:
        return (num, (),)
    a = (a0 + m) // d

    starting = (m, d, a)
    repeating = [a]

    while True:
        m = d * a - m
        d = (num - m ** 2) // d
        a = (a0 + m) // d
        if (m, d, a) == starting:
            break
        repeating.append(a)
    return a0, tuple(repeating)


odd_period = 0
for i in range(2, 10 ** 4 + 1):
    print(i, end='\r')
    _, rep_block = get_continued_sqrt(i)
    if len(rep_block) % 2:
        odd_period += 1
