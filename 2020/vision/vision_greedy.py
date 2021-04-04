"""
Greedy implementation of the vision problem.

Written by Ooj Amit Srivastava.
"""

from typing import List

def solve(satisfactions : List[int], walkers : List[int]) -> int:
    # Find best pair go back-n-forth
    # Pair goodness = sum(pair) * U-index(pair) + sum(0->pair)

    # This is optimal because the walker would keep going
    # back-n-forth across the pair with highest satisfaction
    # as any other path would bring less total satisfaction.
    # easy and intuitive to spot if you draw any array.

    scores = {u: [] for u in walkers}
    # there is a max telescope that a walker can reach
    # which is equal to its u.
    for i in range(min(len(satisfactions), max(walkers)) - 1):
        for w in walkers:
            if i >= w:
                break
            turns = w-i
            # remaining turns would be spent going back-n-forth
            value = ((turns+1)//2)*satisfactions[i] + (turns//2)*satisfactions[i+1]
            # sum of S to reach best pair
            cost = sum(satisfactions[:i])
            scores[w].append(value+cost)

    # Since "cost" is added to each score
    # The max score is optimal path
    # and can be added to total
    total = 0
    for u in walkers:
        total += max(scores[u])

    return total

if __name__ == "__main__":
    t, w = input().split()

    # Satisfaction for ith telescope
    # S = [1, 2, 3, -1, -1, 10]
    S = [int(input()) for _ in range(int(t))]
    # Path length of jth walker
    # U = (23, 24)
    U = [int(input()) for _ in range(int(w))]

    print(solve(S, U))
