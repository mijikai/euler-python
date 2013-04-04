#!/usr/bin/env python3
r"""Given a shape
   A
    \
     F    B
   /   \ /
  J     G
 / \   /
E   I-H-C
     \
      D

where A, .., J is in set {1..10}, not equal to each other, A < B, C, D and
E, and the sum of A + F + G == B + G + H == C + H + I == D + I + J == E + J +
F, find the largest 16-digit concatinated number AFGBGHCHIDIJEJF.
"""    
from itertools import permutations, chain


def solve(side):
    len_set = side * 2
    num_set = set(range(1, len_set + 1))
    tmp = set()
    solutions = []

    for comb in permutations(num_set, len_set):
        comb_list = list(comb)
        outer, inner = comb_list[0:side], comb_list[side:len_set]
        solution_list = []
        for i, o in enumerate(outer):
            sol = (o, inner[i], inner[(i + 1) % side])
            solution_list.append(sol)
        summa = tuple(map(sum, solution_list))
        if summa and all(map(lambda x: x == summa[0], summa)):
            srt = tuple(sorted(solution_list))
            if srt not in tmp:
                tmp.add(srt)
                solutions.append(solution_list)

    return solutions


def main():
    solutions = solve(5)
    append_all = lambda x: ''.join(map(str, chain.from_iterable(x)))

    concat_nums = map(append_all, solutions)
    len_of_16 = filter(lambda x: len(x) == 16, concat_nums)
    ans = max(map(int, len_of_16))
    print(ans)


if __name__ == '__main__':
    main()
