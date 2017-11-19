#!/usr/bin/env python3
"""
Question 1: Promenade Fractions

      1/1
    L     R
   2/1   1/2
3/1         1/3
"""

numerator = 1
denominator = 1

def iterate(directions, left, right):
    l, m = left
    r, s = right

    o = (l + r), (m + s)

    if len(directions) >= 1:
        if directions[0] == 'L':
            return iterate(directions[1:], o, right)
        else:
            return iterate(directions[1:], left, o)

    return o

while True:
    dirs = input()
    print("%d / %d" % iterate(dirs, (1, 0), (0, 1)))

