#!/usr/bin/env python3
"""Let a word be a triangular word if the sum of the letters corresponding to
the position in the English alphabet is a triangular number.
For example, the word SKY is 19 + 11 + 25 = 55, which is a triangular
number."""
import re
from math import floor, sqrt


def sum_letters(word):
    """Find the sum of the position of letters corresponding to the alphabet
    Only accept capital letters.
    Example:
    >>> sum_letters('SKY')
    55
    """
    assert word.isupper()
    excess = ord('A') - 1
    return sum(map(ord, word)) - len(word) * excess


def is_triangular(num):
    """Returns True if ``num`` is a triangular number, otherwise False. A
    number is triangular if for some n, the number is equal to:
        n * (n + 1) / 2
    Example:
    >>> is_triangular(1)
    True
    >>> is_triangular(25)
    False
    >>> is_triangular(55)
    True
    """
    discriminant = 8 * num + 1
    return floor(sqrt(discriminant)) ** 2 == discriminant


def main():
    with open('words.txt') as f:
        words = re.findall('"([^"]*)",?', f.read())
    no_of_trian_words = len(tuple(
        filter(lambda w: is_triangular(sum_letters(w)), words)))
    print(no_of_trian_words)


if __name__ == '__main__':
    print(__doc__)
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
