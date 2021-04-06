"""
2014: Q3 "Increasing passwords"

This is a classic Q3 combinatorics question, with some dynamic programming
thrown in. The key is to find the recurrence relation, and calculate it in a
fast enough way.

Hopefully it's not a huge leap to spot that a valid password beginning with A of
length N can be A followed by either [all of the passwords of length (N - 1)
beginning with B, all of the passwords of length (N - 2) beginning with C, ...].

You can write this out as a table

+------+-------+-------------+-----+
|      |   1   |     2       | ... |
+------+-------+-------------+-----+
| A    |   1   | B+C+D+E+... |     | 
| B    |   2   | C+D+E+...   |     | 
| etc. |       |             |     |
+------+-------+-------------+-----+

This 2D grid should scream dynamic programming to you, but tbh I think in this case
in a language like Python, it seems way easier to just memoise the results using a
dictionary.
"""


def count(begins_with, length, memos):
    assert length <= 36 and length > 0
    assert begins_with >= 0 and begins_with < 36

    if length == 0:
        return 0
    if length == 1:
        return 1

    if (begins_with, length) in memos:
        return memos[begins_with, length]

    result = sum(count(i, length - 1, memos) for i in range(begins_with + 1, 36))

    memos[begins_with, length] = result
    return result


translate_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
assert len(translate_char) == 36


def count_char(char, length):
    return count(translate_char.find(char), length, {})


def compute_length_of_nth_password_and_number_of_shorter_passwords(nth, memos):
    cumulative = 0
    shorter_passwords = 0

    for length_candidate in range(1, 37):
        for c in range(36):
            this_count = count(c, length_candidate, memos)
            cumulative += this_count

            if cumulative >= nth:
                return length_candidate, shorter_passwords

        shorter_passwords = cumulative

    raise RuntimeError("n is too large.")


def solve(nth):
    result = []
    memos = {}

    # Start by figuring out what the length should be, and how many passwords
    # we're skipping over due to length.
    (
        length,
        shorter_passwords,
    ) = compute_length_of_nth_password_and_number_of_shorter_passwords(nth, memos)
    nth -= shorter_passwords

    # Then compute each character individually.
    previous_character = -1

    while length > 0:
        cumulative = 0

        for c in range(previous_character + 1, 36):
            cumulative += count(c, length, memos)

            if cumulative >= nth:
                result.append(translate_char[c])
                previous_character = c
                break

        nth = nth - (cumulative - count(previous_character, length, memos))
        length -= 1

    return "".join(result)


if __name__ == "__main__":
    nth = int(input())
    print(solve(nth))
