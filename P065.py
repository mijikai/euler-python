#!/usr/bin/env python3
"""Find the sum of the digits of the 100th convergent numerator of
the continued fraction for e."""
from fractions import Fraction
pre_e_cont = (1 if (i + 1) % 3 else ((i + 2) // 3) * 2 for i in
        range(100))
next(pre_e_cont)
e_cont = list(pre_e_cont)
e_cont.insert(0, 2)
while e_cont:
    d = Fraction(e_cont.pop())
    try:
        a = e_cont.pop()
    except IndexError:
        e_cont.append(d)
        break
    new_d = a + 1 / d
    e_cont.append(new_d)

print(sum(map(int, str(e_cont.pop().numerator))))
