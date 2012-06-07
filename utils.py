from itertools import chain as _chain, takewhile as _takewhile
from itertools import combinations_with_replacement as _comb_w_rep
from itertools import combinations as _combinations
from itertools import permutations as _permutations, dropwhile as _dropwhile
from math import floor as _floor, sqrt as _sqrt


with open('primes.txt') as prime_f:
    primes = tuple(map(int, prime_f.readlines()))
del prime_f


def digitsof(integer):
    """Make an iterable of the digits of integer starting from the left."""
    return map(int, str(integer))


def power_comb_with_repetition(iterable, n=None):
    """Generate all the combination of iterable of length zero to n. If n is
    None, generete the sequence up to length of iterable."""
    seq = tuple(iterable)
    if n is None:
        n = len(seq)
    return _chain.from_iterable(_comb_w_rep(seq, i)
            for i in range(n + 1))


def is_prime(integer):
    """Returns True if ``integer`` is a prime, otherwise False."""
    assert integer < primes[-1] ** 2
    integer = -integer if integer < 0 else integer
    limit = _floor(_sqrt(integer)) + 1
    for i in _takewhile(lambda elem: elem < limit, primes):
        if integer % i == 0:
            return False
    return integer > 1


def towhole(iterable):
    """Generate a whole number out of the elements of iterable from left to
    right.
    Example:
    >>> towhole([1,2,3])
    123
    """
    num = 0
    seq = tuple(iterable)
    for i in seq:
        if i > 9 and i < 0:
            raise ValueError('iterable composed of negative'
                    ' or non-one-digit number: {}'.format(seq))
        num = 10 * num + i
    return num


def powerset(iterable):
    """Generate another iterable composed of tuple that is a subset of iterable
    Example:
    >>> list(powerset([1,2,3]))
    [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """
    seq = tuple(iterable)
    return _chain.from_iterable(map(lambda i: _combinations(seq, i),
        range(len(seq) + 1)))


def powerset_reverse(iterable):
    seq = tuple(reversed(iterable))
    return _chain.from_iterable(map(lambda i: _combinations(seq, i),
        range(len(seq), 0, -1)))


def partition(iterable):
    seq = tuple(iterable)
    if len(seq) == 0:
        yield []
    if len(seq) == 1:
        yield [seq]
    if 0 <= len(seq) <= 1:
        return

    for i in range(len(seq)):
        i += 1
        head = seq[:i]
        tail = seq[i:]
        for j in partition(tail):
            j.insert(0, head)
            yield j


def digits_int(iterable):
    """Generate an integer from ``iterable``.
    For example:
    >>> digits_int([1, 2, 3])
    123
    """
    integer = 0
    for i in iterable:
        integer = integer * 10 + i
    return integer


def unique_n_digits(digits, n):
    """Generate a generator which yields an n-digit pandigital number. A
    pandigital number has no digits that are the same. 10248 is pandigital
    while 20883 is not.
    """
    lower = 10 ** (n - 1) - 1
    return _dropwhile(lambda num: num <= lower,
            map(digits_int, _permutations(digits, n)))


def runner(func):
    from __main__ import __doc__
    from timeit import Timer
    print(__doc__)
    stmt = 'from __main__ import {0}; {0}()'.format(func)
    print('time =', Timer(stmt=stmt).timeit(1))

# vi: tw=79
