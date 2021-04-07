import raiders

from collections import defaultdict

from hypothesis import given
from hypothesis import strategies as st

def check(starting, swaps):
    positions = {x: i for i, x in enumerate(starting)}
    pattern = starting.copy()

    for (l, r) in swaps:
        li = positions[l]
        ri = positions[r]

        positions[l] = ri
        positions[r] = li

        tmp = pattern[ri]
        pattern[ri] = pattern[li]
        pattern[li] = tmp

    return pattern == list(range(len(starting)))

def test_example():
    solution = raiders.solve([ 0, 4, 2, 1, 3, 5 ])

    assert check([ 0, 4, 2, 1, 3, 5 ], solution)

@given(st.data())
def test_raiders(data):
    size = data.draw(st.integers(min_value=2, max_value=100))
    starting = list(range(size + 2))
    pattern = starting.copy()
    num_swaps = data.draw(st.integers(min_value=1, max_value=(size // 2)))
    possible_swaps = list(
        (x, y)
        for x in range(1, size + 1)
        for y in range(1, size + 1)
        if x != y and x != 0 and y != 0 and x != size + 1 and y != size + 1 and x < y
    )
    used = set()

    for i in range(num_swaps):
        (left, right) = data.draw(st.sampled_from(possible_swaps))
        while (left, right) in used:
            (left, right) = data.draw(st.sampled_from(possible_swaps))
        used.add((left, right))
        possible_swaps.remove((left, right))

        tmp = pattern[left]
        pattern[left] = pattern[right]
        pattern[right] = tmp

    # raiders.solve(pattern)
    # print(num_swaps, pattern)

    starting_pattern = pattern.copy()

    solution = raiders.solve(pattern)

    assert check(starting_pattern, solution), "starting pattern: %s, solution: %s" % (starting_pattern, solution)
