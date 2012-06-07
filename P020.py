#!/usr/bin/env python3


def factorial(num):
    if num < 0 and not isinstance(num, int):
        return 0

    if num == 0:
        return 1

    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


def sum_digits(num):
    result = 0
    while num:
        result += num % 10
        num //= 10

    return result

print(sum_digits(factorial(10000)))
