"""
BIO Q3:

This is basically a combinatorics question (like most BIO Q3s), and I found it
weirdly difficult to get exactly the right answer, and realistically I think I'd
have got this wrong in an exam setting :(.

The trick here is to notice that all of the parameters p, q and r are very
small, so anything involving those numbers can be pretty inefficient if you
need, but n can be very big (watch out if you're using C++ where your ints might
default to 32 bit).

Roughly the first part of the question involves writing a function to find the
number of possible strings with a particular prefix. In this case, this number
only depends only on the number of repeated characters at the end of the string,
and the total number of remaining characters.

To find the correct value, you repeatedly iterate through your list of possible
characters, see whether all the previous characters, and this character take you
past [n], and if so, you know that this is the right character in this position.
You then do this repeatedly until you build up a complete string.

This solution gets full marks :) 27/27

b) CCA is 39th; CCABABCC is 29947th

   I basically binary searched for these myself by guessing and improving, but
   you could automate it if you want

(3/3)

c)

It must be the (unique) middle plan, so there must be an odd number of plans.
There must be an odd number of letters (since there are equal numbers of plans
starting with each character by symmetry) i.e. p is odd.

(3/5)

"""

from functools import lru_cache


@lru_cache(maxsize=None)
def count(remaining_characters, last_char, last_char_count, max_char_count, letters):
    if last_char_count is not None and last_char_count > max_char_count:
        # impossible
        return 0
    elif remaining_characters == 0:
        return 1
    else:
        total = 0

        for i in range(letters):
            if last_char is not None and last_char == i:
                total += count(
                    remaining_characters - 1,
                    last_char,
                    last_char_count + 1,
                    max_char_count,
                    letters,
                )
            else:
                total += count(remaining_characters - 1, i, 1, max_char_count, letters)

        return total


def print_letters(l):
    return "".join(chr(i + ord("A")) for i in l)


letters, max_adjacent, expected_length = tuple(int(x) for x in input().split(" "))

n = int(input()) 
prefix = []
last = None
last_count = 0

while len(prefix) < expected_length:

    for i in range(letters):
        this_last_count = last_count + 1 if i == last else 1
        prefix.append(i)
        with_prefix = count(
            expected_length - len(prefix), i, this_last_count, max_adjacent, letters
        )

        # print("%s - %d" % (print_letters(prefix), with_prefix))

        if with_prefix >= n:
            # this is the right prefix
            last = i
            last_count = this_last_count
            break

        n -= with_prefix
        prefix.pop()

print(print_letters(prefix))

# print(count(1, 0, 1, 2, ))
