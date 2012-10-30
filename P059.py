#!/usr/bin/env python3
"""Find the sum of the ascii equivalent of the decoded text of the cipher. The
encryption is using an xor and the key is a three lowercase letters."""
from itertools import cycle, permutations


def ask_yes_no(prompt=''):
    ans = ''
    while ans not in ('yes', 'no'):
        ans = input(prompt)
    return ans == 'yes'


with open('cipher1.txt') as inp:
    codes_str = inp.read().split(',')
    codes = list(map(int, codes_str))

    # Try all the possible combinations
    for key in permutations(range(*map(ord, 'az')), 3):
        decoded_list = []

        for j, k in zip(codes, cycle(key)):
            decoded_list.append(j ^ k)
        decoded = ''.join(map(chr, decoded_list))

        print(key, end='\r')
        # Try 'the' and 'and'
        if 'the' in decoded and 'and' in decoded:
            print(decoded, key)
            if ask_yes_no('Correct: '):
                print('Sum is', sum(decoded_list))
                break

