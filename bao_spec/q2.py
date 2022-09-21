"""
Q2: Box Constellations

I assume by "opposite" in the question they mean parallel.

Since the number of points is very small, I think my approach is going to be to iterate
over all pairs of points, generate a dictionary of gradient to pairs of points with that
gradient, then iterate over those to find the largest.

The example from the diagram is

10
0 3 1 4 2 4 3 4 4 5 4 3 5 3 2 2 3 1 3 2
"""

import itertools
import math
from typing import List, Tuple
from collections import defaultdict


def group_by_gradient(points: List[Tuple[int, int]]):
    """Transform a list of points into a dictionary from gradient to a list of pairs of
    points that gradient."""

    grouped = defaultdict(list)
    points = sorted(points)

    for i, left in enumerate(points):
        left_x, left_y = left

        for right in points[i + 1 :]:
            right_x, right_y = right

            # since we're sorting, and iterating from i + 1,
            assert right_x >= left_x
            assert left_x != right_x or left_y != right_y

            if right_x - left_x == 0:
                gradient = None
            else:
                gradient = (right_y - left_y) / (right_x - left_x)
            grouped[gradient].append((left, right))

    return grouped


def parse_pairs(input_line):
    """Transforms a string of the form 'x y x y x y' into a list of the form
    `[(x, y), (x, y), (x, y)]`"""
    for i, (x, y) in enumerate(itertools.pairwise(input_line.split(" "))):
        if i % 2 == 0:
            yield (int(x), int(y))


def intercept(pair, gradient):
    """Returns the y-intercept for a pair of points, where x_2 != x_1"""
    ((x_1, y_1), (_x_2, _y_2)) = pair

    return y_1 - gradient * x_1


def vector_length(pair):
    """Returns the length of the vector between the pair of points `pair`."""
    ((x_1, y_1), (x_2, y_2)) = pair

    return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)


def size(first_pair, second_pair, gradient):
    """Returns the size of the quadrilateral formed by the pair of pairs of points
    `first_pair` and `second_pair`."""
    if gradient is None:
        # x is the same for each pair, so just take the difference
        perpindicular_distance = abs(first_pair[0][0] - second_pair[0][0])
    else:
        perpindicular_distance = abs(
            intercept(first_pair, gradient) - intercept(second_pair, gradient)
        ) / math.sqrt(1 + (gradient**2))

    return (
        (vector_length(first_pair) + vector_length(second_pair)) / 2
    ) * perpindicular_distance


def main():
    _count = input()
    points = list(parse_pairs(input()))

    # then, pick the largest

    best_size = None

    for gradient, pairs in group_by_gradient(points).items():
        for i, left in enumerate(pairs):
            for right in pairs[i + 1 :]:
                this_size = size(left, right, gradient)
                if best_size is None or this_size > best_size:
                    best_size = this_size

    print(f"{best_size:.2f}")


if __name__ == "__main__":
    main()
