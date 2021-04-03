"""2016 Q3: prime connections"""

from typing import Optional, List
from heapq import heappush, heappop


def find_primes(prime_limit):
    primes = set()
    numbers: List[Optional[int]] = list(range(0, prime_limit + 1))

    numbers[0] = None
    numbers[1] = None

    for i in range(2, prime_limit + 1):
        if numbers[i] is None:
            continue

        primes.add(i)

        for j in range(2 * i, prime_limit + 1, i):
            numbers[j] = None

    return primes


def shortest_path(primes, start, end):
    seen = {start}
    q = [(1, start)]

    while len(q) > 0:
        (prev_len, node) = heappop(q)

        if node == end:
            return prev_len

        for i in range(24):
            diff = 1 << i

            next_one = node + diff
            if next_one in primes:
                t = (prev_len + 1, next_one)
                if next_one not in seen:
                    seen.add(next_one)
                    heappush(q, t)

            next_one = node - diff
            if next_one in primes:
                t = (prev_len + 1, next_one)
                if next_one not in seen:
                    seen.add(next_one)
                    heappush(q, t)

    print("Not found")
    return None


def solve(prime_limit, start, end):
    """
    1. Find all of the primes <= prime_limit
    2. BFS to find the minimum distance between start and end
    """

    primes = find_primes(prime_limit)
    return shortest_path(primes, start, end)


if __name__ == "__main__":
    prime_limit, start, end = tuple(int(x) for x in input().split())

    print(solve(prime_limit, start, end))
