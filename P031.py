#!/usr/bin/env python3
"""How many different ways can a two pound be made out of:
    1p, 2p, 5p, 10p, 20p, 50p, 1 pound, 2 pound
"""
from functools import lru_cache


def make_change(coins, value):
    """Returns the number of combinations of ``coins``
    to make up ``value``"""
    @lru_cache(maxsize=None)
    def make_change_helper(coins, value):
        if value == 0:
            return 1
        if not coins or value < -1:
            return 0

        coins = tuple(coins)
        combi = 0
        combi += make_change_helper(coins, value - coins[0])
        combi += make_change_helper(coins[1:], value)
        return combi
    return make_change_helper(coins, value)


def main():
    coins = (1, 2, 5, 10, 20, 50, 100, 200)  # denomination
    target = 200  # two pound
    print(make_change(coins, target))


if __name__ == '__main__':
    print(__doc__)
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
