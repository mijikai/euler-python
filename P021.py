#!/usr/bin/env python3
import math


def make_sieve(upper):
    """Returns a list of prime numbers from 2 to upper inclusive using the
    sieve of Eratosthenes."""

    if upper <= 0:
        return []

    sieve = [True for i in range(upper + 1)]
    limit = math.floor(math.sqrt(upper))
    sieve[0], sieve[1] = False, False

    for i in range(2, limit + 1):
        if sieve[i]:
            for j in range(i * 2, upper + 1, i):
                sieve[j] = False

    primes = []
    for num, is_prime in enumerate(sieve):
        if is_prime:
            primes.append(num)

    return primes


def prime_factorization(num):
    """Returns a dictionary where the keys are the prime factors of the number
    and values are the power of each prime."""
    return prime_factors_p(num, _sieve)


def prime_factors_p(num, primes):
    """Returns a dictionary of primes whose value is its power that are the
    factor of num."""
    if num > primes[len(primes) - 1]:
        raise Exception('num is larger than the largest prime in the list: '
                '{} > {}'.format(num, primes[len(primes) - 1]))
    factors = {}
    if num < 0:
        factors[-1] = 1
        num = -num

    limit = math.floor(math.sqrt(num))

    current = num
    for i in primes:
        if i > current or i > limit:
            if current != 1:
                factors[current] = 1
            break
        power = 0
        while current % i == 0:
            power += 1
            current //= i

        if power > 0:
            factors[i] = power

    return factors


def product(iterable):
    """Returns the product of all numbers in the iterable."""
    prod = 1
    for i in iterable:
        prod *= i
    return prod


def divisor(k, num):
    """Returns the sum of the kth power of the integer divisors of num."""

    if k < 0:
        raise Exception('k must be >= 0: {}'.format(k))

    factors = prime_factorization(num)
    result = 1
    if k == 0:
        for prime in factors:
            result *= prime + 1

    for prime in factors:
        result *= ((pow(prime, (factors[prime] + 1) * k) - 1) //
                (prime ** k - 1))
    return result


def aliquot_sum(k, num):
    """Returns the aliquot sum of the kth power of the integer divisors of
    num."""
    return divisor(k, num) - num ** k


def is_amnicable(num):
    """Returns True if num is an amnicable number."""

    # Because d(m) = d(n) = s(m) + s(n)
    # so d(s(m) - m) = d(n)
    result = divisor(1, num)

    # s(n) and n is supposed to be
    # different numbers so not amnicable
    if 2 * num == result:
        return False

    result2 = divisor(1, result - num)
    return result == result2


def sum_amnicable(limit):
    """Returns the sum of all amnicable numbers below limit."""
    return sum(map(lambda num: num * is_amnicable(num), range(2, limit)))


def main():
    global _sieve, _limit
    _limit = 10 ** 6
    _sieve = make_sieve(_limit)
    given = 10 ** 4

    print(sum_amnicable(given))


def main2():
    # much more elegant solution https://projecteuler.net/thread=21
    # from gamepower

    # the indices are the num and the value are the sum of the divisors of num
    given = 10 ** 4
    sum_of_divisors = [0 for i in range(given)]
    sum_of_amnicables = 0
    for i in range(1, given):
        for j in range(i * 2, given, i):
            sum_of_divisors[j] = sum_of_divisors[j] + i

    for i in range(2, given):
        if i < sum_of_divisors[i] < given:
            if sum_of_divisors[sum_of_divisors[i]] == i:
                sum_of_amnicables += sum_of_divisors[i] + i

    print(sum_of_amnicables)

if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
