#!/usr/bin/env python3
"""How many n-digit number is an nth power of another number
where n is a positive integer?"""
from itertools import takewhile, count
from math import ceil

def nlen_nthpower(n):
    lower = ceil(10 ** ((n - 1) / n))
    return 10 - lower

print(sum(takewhile(lambda x: x, map(nlen_nthpower, count(1)))))

