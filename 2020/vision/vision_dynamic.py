from typing import List, Optional
from collections import Counter


def max_opt(l, r):
    return r if l is None else l if r is None else max(l, r)


def solve(satisfactions: List[int], steps: List[int]) -> int:
    walkers = Counter(steps)

    max_satisfaction: List[Optional[int]] = [
        None for _ in range(len(satisfactions))
    ]
    max_satisfaction[0] = satisfactions[0]

    total = 0 

    if 1 in walkers:
        total += walkers[1] * satisfactions[0]

    for i in range(max(steps) - 1):
        max_score = None
        next_scores: List[Optional[int]] = [None for _ in satisfactions]

        for position in range(len(satisfactions)):
            # Lookup the scores from the previous step.
            left_score = max_satisfaction[position - 1] if position - 1 >= 0 else None
            right_score = (
                max_satisfaction[position + 1]
                if position + 1 < len(max_satisfaction)
                else None
            )

            # The best route is going from the adjacent telescope with the best
            # score on the previous step to this telescope.
            best_choice = max_opt(left_score, right_score)
            best_choice = best_choice + satisfactions[position] if best_choice is not None else None

            # Keep track of the best score for this telescope to use next time.
            next_scores[position] = best_choice

            max_score = max_opt(max_score, best_choice)

        # We use (i + 2), since we implicitly have a first step with the initial
        # setup, and then we start counting from zero in this loop.
        if (i + 2) in walkers:
            if max_score is not None:
                total += walkers[i + 2] * max_score
            else:
                raise RuntimeError("BUG: max score not found.")

        max_satisfaction = next_scores

    return total


if __name__ == "__main__":
    telescopes, walkers = input().split()

    telescopes = int(telescopes)
    walkers = int(walkers)

    satisfactions = [int(input()) for _ in range(telescopes)]
    steps = [int(input()) for _ in range(walkers)]

    print(solve(satisfactions, steps))
