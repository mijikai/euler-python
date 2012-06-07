#!/usr/bin/env python3
"""Given t, p, and h where t = a(a - 1)/2, p = b*(3n-1)/2 and h = c(2c - 1),
find h so that t = p = h
"""
from math import sqrt, floor
from itertools import count
from utils import runner


def main():
    number = 0
    for i in count(1):
        hexa = i * (2 * i - 1)
        penta_ind = (1 + sqrt(1 + 24 * hexa)) / 6
        if penta_ind.is_integer():
            print(hexa)
            number += 1
            if number == 3:
                break


if __name__ == '__main__':
    runner('main')
