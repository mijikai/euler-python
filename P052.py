#!/usr/bin/env python3
"""Find the smallest number x such that 2 * x, 3 * x , 4 * x, 5 * x and 6 * x
are permutations of x."""
from itertools import count
from utils import runner


def main():
    for j in count(1):
        found = True
        numstr = tuple(sorted(str(j)))
        for k in range(1, 7):
            if tuple(sorted(str(k * j))) != numstr:
                found = False
                break
        if found:
            print(j)
            break


if __name__ == '__main__':
    runner('main')
