#!/usr/bin/env python3
import num_theory


def greatest_lower_bound(lst, num):
    start = 0
    end = len(lst) - 1
    elem = ()

    while start <= end:
        middle = (end + start) // 2
        mid_elem = lst[middle]
        if num < mid_elem:
            end = middle - 1
        elif num > mid_elem:
            elem = (middle, mid_elem)
            start = middle + 1
        else:
            elem = (middle, mid_elem)
            break

    return elem


def least_upper_bound(lst, num):
    start = 0
    end = len(lst) - 1
    elem = ()

    while start <= end:
        middle = (end + start) // 2
        mid_elem = lst[middle]
        if num < mid_elem:
            elem = (middle, mid_elem)
            end = middle - 1
        elif num > mid_elem:
            start = middle + 1
        else:
            elem = (middle, mid_elem)
            break

    return elem


def abundant_numbers(upper):
    """List all abundant numbers up to ``upper`` exclusive."""

    return [num for num, divisor_sum in
            enumerate(num_theory.sum_of_divisors(upper))
            if 2 * num < divisor_sum]


def is_sum_of_abundant(num, abundant=None):
    """Returns True if num can be written as the sum of two abundant
    numbers."""
    if abundant is None:
        abundant = abundant_numbers(num)

    glb = greatest_lower_bound(abundant, num // 2)
    if glb:
        max_ind = glb[0]
    else:
        return False

    for i in range(max_ind, -1, -1):
        x = abundant[i]
        y = num - x
        if y in abundant:
            return True
    return False


def main():
    upper = 20161 + 1
    abundant_list = abundant_numbers(upper)

    summation = sum(filter(lambda x: not is_sum_of_abundant(x,
        abundant_list), range(1, upper + 1)))
    print(summation)


def main2():
    upper = 20161 + 1
    abundant_list = abundant_numbers(upper)
    is_sum_of_two = [False for i in range(upper)]

    for i in abundant_list:
        for j in abundant_list:
            if i + j < len(is_sum_of_two):
                is_sum_of_two[i + j] = True
            else:
                break
    print(sum(i for i, j in enumerate(is_sum_of_two) if not j))


if __name__ == '__main__':
    from timeit import Timer
    t = Timer(stmt='from __main__ import {0}; {0}()'.format('main2'))
    print(t.timeit(1))
