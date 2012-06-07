#!/usr/bin/env python3
"""Find the last ten digits of the expansion 1 ** 1 + 2 ** 2 + 3 ** 3 + ... +
1000 ** 1000."""
from utils import runner


def main():
    significant = 10
    limit = 10 ** 3
    pow_ten = 10 ** significant
    res = sum(map(lambda num: pow(num, num, pow_ten),
        range(1, limit + 1))) % pow_ten
    print(res)


if __name__ == '__main__':
    runner('main')
