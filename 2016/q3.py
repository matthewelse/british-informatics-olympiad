"""2016 Q3: prime connections"""

from math import log2
from collections import deque

def find_primes(prime_limit):
    primes = set()

    # For a performance hack, you can swap this for an array, but as it is, a
    # list is just about fast enough.
    #
    # numbers = array.array('L', range(0, prime_limit + 1))
    numbers = list(range(0, prime_limit + 1))

    numbers[0] = 0
    numbers[1] = 0

    for i in range(2, prime_limit + 1):
        if numbers[i] == 0:
            continue

        primes.add(i)

        for j in range(2 * i, prime_limit + 1, i):
            numbers[j] = 0

    return primes


def shortest_path(primes, start, end, max_prime):
    q = deque([(1, start)])
    upper_bit_limit = int(log2(max_prime)) + 1
    primes.remove(start)

    while len(q) > 0:
        (prev_len, node) = q.popleft()

        if node == end:
            return prev_len

        for i in range(upper_bit_limit):
            diff = 1 << i

            next_one = node + diff
            if next_one in primes:
                primes.remove(next_one)
                q.append((prev_len + 1, next_one))

            next_one = node - diff
            if next_one in primes:
                primes.remove(next_one)
                q.append((prev_len + 1, next_one))

    print("Not found")
    return None


def solve(prime_limit, start, end):
    """
    1. Find all of the primes <= prime_limit
    2. BFS to find the minimum distance between start and end
    """

    primes = find_primes(prime_limit)
    return shortest_path(primes, start, end, prime_limit)


if __name__ == "__main__":
    prime_limit, start, end = tuple(int(x) for x in input().split())

    print(solve(prime_limit, start, end))
