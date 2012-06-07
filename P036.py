#!/usr/bin/env python3
"""Find the sum of all numbers less than one million that are pallindrome in
base 2 and base 10."""
from itertools import chain


def is_pallindrome(integer, base=10):
    """Returns True if ``integer`` is a pallindrome in base ``base``
    otherwise False."""
    assert isinstance(integer, int)
    digits = []
    integer = abs(integer)
    num = integer
    while num:
        digits.append(num % base)
        num //= base
    return list(digits) == list(reversed(digits))


def generate_pallindrome(digitslength, includezero=False):
    """Generate pallindromes in base ten of length ``digitslength``. If
    ``includezero`` is True, numbers with zero at the front and end are also
    returned. The sequence generated is not sored."""
    assert digitslength > 0
    if includezero:
        start = 0
    else:
        start = 1
    end = 10
    if digitslength <= 2:
        for i in range(start, end):
            yield (digitslength - 1) * i * 10 + i
        return 
    for i in generate_pallindrome(digitslength - 2, True):
        for j in range(start, end):
            num = j
            num = num * 10 ** (digitslength - 2) + i
            num = num * 10 + j
            yield num

            
def main():
    def condition(elem):
        return elem % 2 != 0 and is_pallindrome(elem, 2)

    limit = 7
    pallindrome_base_ten = chain.from_iterable(
            map(generate_pallindrome, range(1, limit)))
    pallindromes = tuple(filter(condition, pallindrome_base_ten))
    for i in pallindromes:
        print(i)
    print('Sum is {}'.format(sum(pallindromes)))


if __name__ == '__main__':
    print(__doc__)
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
