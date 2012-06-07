#!/usr/bin/env python3
import math

ones = ['one', 'two', 'three', 'four', 'five',
    'six', 'seven', 'eight', 'nine']
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty',
    'sixty', 'seventy', 'eighty', 'ninety']
elev_to_nineteen = ['eleven', 'twelve', 'thirteen', 'forteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
hund = 'hundred'
and_ = 'and'


def count_ones():
    """Count the total letters use from 1 to 9 inclusive"""
    return sum(map(len, ones))


def count_tens():
    """Count the total letters use from 10 to 99 inclusive"""
    _tens = tens[1:] # exlude ten from count
    ones_len = count_ones()

    elev_sum = sum(map(len, elev_to_nineteen))
    rest_sum = len(tens[0])
    rest_sum += sum(len(i) * 10 + ones_len for i in _tens)
    return elev_sum + rest_sum


def count_hundreds():
    """Count the total letters from 100 to 999 inclusive"""
    hundred_len = (len(i) + len(hund) + len(and_) for i in ones)
    ones_len = count_ones()
    tens_len = count_tens()
    return sum(i * 100 + tens_len + ones_len for i in hundred_len)


def main():
    thou = len(ones[0]) + len('thousand')
    print(count_ones() + count_tens() + count_hundreds() + len('one') + thou)


if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
