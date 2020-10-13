"""
How many distinct look and says are there from 1 to 3999?

Reuse the functions from part a, and just loop. Use a set to filter out duplicates.

Answer is 3919.
"""

import q1

looks_and_says = set()

for i in range(3999):
    n = i + 1

    look_and_say = q1.look_and_say(q1.roman(n))

    looks_and_says.add(look_and_say)

print(len(looks_and_says))

