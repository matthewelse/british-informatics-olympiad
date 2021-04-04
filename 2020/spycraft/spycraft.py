"""
I think I've managed to convince myself that the way to solve this problem is to
treat this as a shortest path problem.
"""

from heapq import heappush, heappop


def distance_between(from_, to):
    x0, y0 = from_
    x1, y1 = to

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    diagonal_moves = min(dx, dy)

    return dx + dy - diagonal_moves


def shortest_path(boxes, start, end):
    q = []

    for corner in boxes[start]:
        heappush(q, (0, start, corner))

    while len(q) > 0:
        (distance, box, corner) = heappop(q)

        if box == end:
            return distance

        for next_corner in boxes[box + 1]:
            heappush(
                q,
                (
                    distance + distance_between(corner, next_corner),
                    box + 1,
                    next_corner,
                ),
            )

    raise RuntimeError("Route not found.")


if __name__ == "__main__":
    num_contacts = int(input())

    boxes = []

    for i in range(num_contacts):
        x0, y0, x1, y1 = tuple(int(x) for x in input().split())

        corners = {(x0, y0), (x1, y1), (x1, y0), (x0, y1)}

        boxes.append(corners)

    print(shortest_path(boxes, start=0, end=len(boxes) - 1))
