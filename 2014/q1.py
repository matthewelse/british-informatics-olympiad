"""
Q1: Lucky Numbers

This is very similar to the idea of a sieve of eratosthenes, an algorithm for
finding prime numbers. I've done a pretty slow implementation, but it's fast enough.
"""


def solve(nearest):
    """
    Iterate through the numbers, and cross out non-lucky numbers as we go along.
    We'll also calculate lower and higher as we go along. We'll denote
    'crossed-out' numbers using zero.
    """

    # I'm sure there's a way of proving that this will always include what we're
    # looking for. Maybe we should pass the multiplicative factor as an argument
    # and try again if we fail the first time?
    numbers = [2 * n + 1 for n in range(nearest)]

    lower = 1

    for i in range(1, len(numbers)):
        step = numbers[i]
        if step == 0:
            continue
        else:
            if step < nearest:
                lower = step
            elif step > nearest:
                # Once we find the first value greater than what we're looking for, return.
                return (lower, step)

            seen = 1
            for i in range(0, len(numbers)):
                old = numbers[i]

                if seen % step == 0:
                    numbers[i] = 0

                if old != 0:
                    seen += 1

    raise RuntimeError("Unable to find bounding lucky numbers. (input: %d)" % nearest)


if __name__ == "__main__":
    search_for = int(input())
    lower, higher = solve(search_for)

    print("%d %d" % (lower, higher))
