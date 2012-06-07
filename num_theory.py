#!/usr/bin/env python3
from math import ceil as _ceil, sqrt as _sqrt, floor as _floor
from itertools import count as _count, cycle as _cycle, starmap as _starmap
from heapq import heappush as _heappush, heappop as _heappop
from operator import mul as _mul


def sieve_of_eratosthenes(upper):
    """Returns a generator of primes < upper through the use of the sieve of
    Eratosthenes."""
    composites = set()
    yield 2
    yield 3
    i = 3
    for j in range(i ** 2, upper + 1, 2 * i):
        if j % 5 != 0:
            composites.add(j)
    yield 5

    for i in range_step(7, upper + 1, _cycle([2, 2, 2, 4])):
        if i not in composites:
            for j in range(i ** 2, upper + 1, 2 * i):
                if j % 5 != 0:
                    composites.add(j)
            yield i
        else:
            composites.remove(i)


def sum_of_divisors(upper, k=1):
    """Returns a list of length upper whose values correspond to the sum of
    the divisor raise to k of the index."""
    lst = [i ** k for i in range(upper)]

    for i in range(1, upper):
        for j in range(2 * i, upper, i):
            lst[j] += i ** k
    return lst


def range_step(start, stop=None, step=None):
    """Like range but step is an iterator. If iterator is exhausted, the last
    value will be use as the step."""
    if stop is None:
        stop = start
        start = 0
    if step is None:
        step = _cycle([1])

    current = start
    while current < stop:
        yield current
        try:
            current_step = next(step)
        except StopIteration:
            step = _cycle(current_step)
        current += current_step


def pythagorean_triples(n=None):
    """Generate n Pythagorean triples ordered by the value of c ascending. If n
    is None or not given, generate infinitly. Default is None.
    Examples:
    >>> list(pythagorean_triples(5))
    [(3, 4, 5), (5, 12, 13), (15, 8, 17), (7, 24, 25), (21, 20, 29)]
    """
    iterator = _count() if n is None else range(n)
    iterator = iter(iterator)

    base_mat = ((1, 2, 2),
            (2, 1, 2),
            (2, 2, 3))
    multiplier = ((1, -1, 1), (1, 1, 1), (-1, 1, 1))
    matrices = []
    for multip in multiplier:
        mat = []
        for row, elem in zip(base_mat, multip):
            mat.append(tuple(map(lambda e: e * elem, row)))
        matrices.append(tuple(mat))
    matrices = tuple(matrices)

    heap = [(5, (3, 4, 5))]
    for i in iterator:
        _, triple = _heappop(heap)
        yield triple
        for matrix in matrices:
            next_triple = tuple(map(lambda col: sum(_starmap(_mul,
                zip(triple, col))), zip(*matrix)))
            _heappush(heap, (next_triple[2], next_triple))


def is_prime(num):
    """Returns True if num > 0 is a prime, otherwise False."""
    assert num > 0
    return num == 2 or num > 1 and num % 2 != 0 and miller_prime_test(num)


def miller_prime_test(num):
    """Determine the primality of the number by using the fact that a number is
    probably a prime if:
        n - 1 = a ** (d * 2 ** s ) s > 0, d is odd
        a ** d = 1 % n or (a ** d) ** 2 ** r = -1 % n, 0 <= r < s
    """
    test_base = [i for i in (2, 7, 61) if i < num]
    d = num - 1
    minus_one = num - 1
    s = 0
    while d and d % 2 == 0:
        d >>= 1
        s += 1
    for a in test_base:
        probably_prime = False
        x = pow(a, d, num)
        if x in (1, minus_one):
            continue
        for r in range(1, s):
            x = pow(x, 2, num)
            if x == minus_one:
                probably_prime = True
                break
        if not probably_prime:
            return False
    return True
