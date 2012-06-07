#!/usr/bin/env python3

def nth_permutation(n, string):
    """Returns the nth permutation of the string. The index is zero based. If n
    > factorial(len(string)), the result wraps up.

    Example:
    >>> nth_permutation(0, '123')
    '123'
    >>> nth_permutation(4, '123')
    '312'
    >>> nth_permutation(6, '123')
    '123'

    """
    result = ''
    no_of_perm = 1
    for i in range(1, len(string)):
        no_of_perm *= i

    is_used = [False for i in range(len(string))]
    curr_n = n % (len(string) * no_of_perm)

    for i in range(len(is_used), 1, -1):
        ind = curr_n // no_of_perm  # the next character not in used
        curr_n = curr_n % no_of_perm  # the nth permutation of i len string
        no_of_perm //= i - 1  # permutation of the i len string

        for pos in range(len(is_used)):
            if not is_used[pos]:
                ind -= 1
                if ind == -1:
                    is_used[pos] = True
                    break

        result += string[pos]

    for pos in range(len(is_used)):
        if not is_used[pos]:
            result += string[pos]
            break

    return result


def main():
    string = '0123456789'
    pos = 10 ** 6 - 1
    print(nth_permutation(pos, string))

if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
