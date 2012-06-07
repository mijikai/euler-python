#!/usr/bin/env python3
"""Get the number of months where Sunday is the first day from year 1901
to 2000."""
from itertools import chain


def is_leap_year(year):
    """Tells whether the ``year`` is a leap year. A leap year occurs
    when a year is divisible by 4 but not by 100 except when it is
    divisible by 400."""
    return (year % 400 == 0 or
            year % 100 != 0 and
            year % 4 == 0)


def month_codes(year):
    """Make a iterable composed of the codes for the first day of the
    months in the given ``year``. Codes are the following:
        * 0 - Sunday
        * 1 - Monday
        * 2 - Tuesday
        * 3 - Wednesday
        * 4 - Thursday
        * 5 - Friday
        * 6 - Sunday

    If the given year is a leap year, adjust the code accordingly.
    Examples:
    >>> list(month_codes(1901))
    [2, 5, 5, 1, 3, 6, 1, 4, 0, 2, 5, 0]
    >>> list(month_codes(1900)) # 1900 is not a leap year
    [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
    """
    base_year = 1901
    codes = [2, 5, 5, 1, 3, 6, 1, 4, 0, 2, 5, 0] # codes for 1901

    # adjustment for March to December if leap year
    adjust_day = int(is_leap_year(year))

    # adjustment from the base year
    adjust_year = ((year - base_year) // 4 *
            int(is_leap_year(year - 1)))

    jan_feb = iter(codes[0:2])
    rest_month = (i + adjust_day for i in codes[2:])
    for i in chain(jan_feb, rest_month):
        yield (year - base_year +  i + adjust_year) % 7


def first_sundays():
    """Count number of months where Sunday is the first day from 1901 to
    2000."""
    init_year = 1901
    final_year = 1950
    months_first_day = chain.from_iterable(map(month_codes,
            range(init_year, final_year + 1)))

    return len(list(filter(lambda code: code == 0, months_first_day)))


def much_shorter():
    def days(year):
        # code for the year 1901 
        return chain(iter([2, 5]),
                map(lambda x: (x +
                        (year % 4 == 0)) % 7,
                    [5, 1, 3, 6, 1, 4, 0, 2, 5, 0]))
        
    return sum(filter(lambda x: x == 1, chain.from_iterable(map(lambda year:
        list(map(lambda month: 1 + (month + (year - 1) // 4 + (year - 1)) % 7,
            days(year))), range(1, 100 + 1)))))


def main():
    print(first_sundays())

if __name__ == '__main__':
    from timeit import Timer
    stmt = 'from __main__ import {0}; {0}()'.format('main')
    print('time =', Timer(stmt=stmt).timeit(1))
