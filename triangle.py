#!/usr/env/python


def file_to_list(filename):
    """Open a file with a name filename and returns a list of list which has a
    relationship of:

    list[m][n] <= list[m + 1][n]
    list[m][n] <= list[m + 1][n + 1]

    for all m and n.

    The file is a list of numbers separated by whitespace with an exception
    of newline and the line is one number less than the next line."""
    with open(filename, 'r') as inp:
        lst = [[int(i) for i in line.split()] for line in inp.readlines()]
    return lst


def max_sum(lst, row=0, col=0, memo=None):
    """Returns the maximum sum from top to bottom in a triangle of numbers.

    lst: a list which satisfy the property lst[m][n] <= lst[m + 1][n] and
        lst[m][n] <= lst[m + 1][n + 1]
    row, col: current position in the list
    memo: the dictionary of (row, col) whose value is the computed max_sum;
        default is None"""

    if memo == None:
        memo = {}

    if row >= len(lst):
        return 0

    if (row, col) in memo:
        return memo[(row, col)]

    left = max_sum(lst, row + 1, col, memo)
    right = max_sum(lst, row + 1, col + 1, memo)

    memo[(row, col)] = lst[row][col] + max(left, right)
    return memo[(row, col)]
