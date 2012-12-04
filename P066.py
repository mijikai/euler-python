#!/usr/bin/env python3
from fractions import Fraction
from itertools import cycle, count
from math import floor, sqrt


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


def get_nth_convergent(n, cont_frac):
    head, rest = cont_frac
    seq = [head]
    if isinstance(rest, tuple):
        r = cycle(rest)
    else:
        r = rest
    for _, i in zip(range(n - 1), r):
        seq.append(i)

    while True:
        d = seq.pop()
        try:
            a = seq.pop()
        except IndexError:
            seq.append(d)
            break
        num = a + Fraction(1, d)
        seq.append(num)
    return Fraction(seq.pop())


maximum = 1000
max_x = 0
D = 0
for i in range(2, maximum + 1):
    continued_frac = get_continued_sqrt(i)
    if not continued_frac[1]:
        continue
    for j in count(1):
        convergent = get_nth_convergent(j, continued_frac)
        x, y = convergent.numerator, convergent.denominator
        if x * x - i * y * y == 1:
            break
    if x > max_x:
        max_x = x
        D = i

print(D, max_x)

