#!/usr/bin/env python3
start = 10
num_permu = 5
while True:
    cube_counter = {}
    start *= 10
    end = start * 10
    for i in range(start, end):
        cube = i ** 3
        sorted_digits = ''.join(sorted(str(cube)))
        val = cube_counter.setdefault(sorted_digits, [cube, 0])
        val[1] += 1

    candidates = []
    for num, count in cube_counter.values():
        if count == num_permu:
            candidates.append(num)

    if candidates:
        candidates.sort()
        print(candidates[0])
        break

