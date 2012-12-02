#!/usr/bin/python3
from math import sqrt, ceil, floor
from itertools import groupby


def polygonal_number(s, n):
    return (n * (n + 1) + (s - 3) * n * (n - 1)) / 2


def inverse_polygonal_number(s, N):
    s = s - 2
    return ((s - 2) + sqrt(s * s + (8 * N - 4) * s + 4)) / (2 * s)


def traverse(graph, sides):
    subgraph = graph[sides[0]]
    rest_sides = sides[1:]
    for head in subgraph.keys():
        tails = subgraph[head]
        for t in tails:
            num = head * 100 + t
            for sol in traverse_helper(t, graph, rest_sides, (num,)):
                if sol[-1] % 100 == head:
                    yield sol


def traverse_helper(head, graph, sides, res):
    if not sides:
        yield res

    for i, s in enumerate(sides):
        subgraph = graph[s]
        sides_list = list(sides)
        sides_list.remove(s)
        try:
            tails = subgraph[head]
        except KeyError:
            continue

        for tail in tails:
            num = head * 100 + tail
            if num in res:
                continue
            for ret in traverse_helper(tail, graph, sides_list, res + (num,)):
                yield ret


inv = inverse_polygonal_number
sides = tuple(range(3, 9))
bounds = ((ceil(inv(i, 1000)), floor(inv(i, 9999))) for i in sides)
pol_nums = tuple(
        tuple(int(polygonal_number(s, n)) for n in range(lower, upper + 1))
            for s, (lower, upper) in zip(sides, bounds))
pol_nums_split = tuple(
        tuple((num // 100, num % 100) for num in seq)
            for seq in pol_nums)
graph_pol = {}
for i, seq in zip(sides, pol_nums_split):
    subgraph = {}
    graph_pol[i] = subgraph
    for init, final in seq:
        subgraph.setdefault(init, [])
        subgraph[init].append(final)

for sol in traverse(graph_pol, sides):
    print(sum(sol), sol)
