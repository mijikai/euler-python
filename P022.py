#!/usr/bin/env python3
import re


def name_score(name, pos):
    """Returns the name score of name.
    The name score is computed as follows:
        score = pos * sum of the alpha ordering of the character name.
    pos is the position starting from 1 of the name from a list
    Example:
        if name is Collin and pos = 934
        sum = 3 + 15 + 12 + 12 + 9 + 14
        score = 934 * sum."""
    name = name.lower()
    sum_alpha_pos = 0
    for i in name:
        sum_alpha_pos += ord(i)
    sum_alpha_pos -= (ord('a') - 1) * len(name)
    return sum_alpha_pos * pos


def main():
    with open('names.txt') as inp:
        list_of_names = re.findall(pattern='(?:\")([^"]*)(?:\"\,?)',
                string=inp.read())

    list_of_names.sort()

    sum_name_score = sum(map(name_score, list_of_names,
        range(1, len(list_of_names) + 1)))
    print(sum_name_score)


if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import main; main()'
    print('time =', Timer(stmt=stmt).timeit(1))
