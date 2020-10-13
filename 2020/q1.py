"""
2020 Q1: Roman Look and Say

25/25

b) 4: II, III, IV, IX [2]
c) 3919 [4]

31 marks
"""


def group(l):
    """
    Group a list into groups of adjacent elements. e.g.

    > group(list("AAABBCCDBBBBA"))
    [("A", 3), ("B", 2), ("C", 2), ("D", 1), ("B", 4), ("A", 1)]
    """

    result = []
    previous = None
    count = 0

    for elem in l:
        if previous is None:
            previous = elem
            count = 1
        elif previous == elem:
            count += 1
        else:
            result.append((previous, count))
            previous = elem
            count = 1

    if previous is not None:
        result.append((previous, count))

    return result


def get_smallest_numeral_greater_or_equal(n):
    """
    It would probably be slightly faster to do this using binary search, but realistically
    this list is so short that it's perfectly fine to just search through it from start to
    finish every time.
    """

    sizes = [
        (1, "I"),
        (4, "IV"),
        (5, "V"),
        (9, "IX"),
        (10, "X"),
        (40, "XL"),
        (50, "L"),
        (90, "XC"),
        (100, "C"),
        (400, "CD"),
        (500, "D"),
        (900, "CM"),
        (1000, "M"),
    ]

    for size, letter in reversed(sizes):
        if size <= n:
            return size, letter

    return (1000, "M")


def roman(n):
    if n == 0:
        return ""

    size, letter = get_smallest_numeral_greater_or_equal(n)
    return letter + roman(n - size)


def look_and_say(s):
    counts = group(s)
    result = []

    for letter, count in counts:
        result.append(roman(count))
        result.append(letter)

    return "".join(result)


if __name__ == "__main__":
    year, n = input().split(" ")
    n = int(n)

    for _ in range(n):
        year = look_and_say(year)

    i_count = year.count("I")
    v_count = year.count("V")

    print("%d %d" % (i_count, v_count))
