"""
Q1: Lucky Numbers

This is very similar to the idea of a sieve of eratosthenes, an algorithm for
finding prime numbers. I've done a pretty slow implementation, but it's fast enough.
"""

search_for = int(input())
numbers = [2 * n + 1 for n in range(10000)]

lower = None
higher = None

for i in range(len(numbers)):
    if i >= len(numbers):
        break
    elif numbers[i] == 1:
        lower = numbers[i]
    else:
        step = numbers[i]

        if step < search_for:
            lower = step
        elif step > search_for:
            higher = step
            break
        
        # Mark every step'th number as not lucky (i.e. set it to -1). Note that
        # we ignore already-marked numbers for the purposes of counting here.
        #
        # This is kind of slow, but I think it's fast enough (only needs to be <
        # 1s). If we want to go faster, we could use a linked list, but Python
        # doesn't have one in its standard library.
        numbers = [n for i, n in enumerate(numbers) if ((i + 1) % step) != 0]

print("%d %d" % (lower, higher))
