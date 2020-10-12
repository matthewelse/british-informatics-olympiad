"""
2019 Q3: Block-chain

This solution is too slow for 3 of the harder examples in the mark scheme, but I'm pretty sure it's
correct. The C++ solution is faster, fast enough for all but the hardest example.

This solution uses depth-first search to enumerate the possible combinations, eliminating invalid
additions by detecting triples of a, b, c where a < b < c as we try to add new blocks to the prefix.
"""


def is_valid_to_add(prefix, new_char, available):
    """
    We assume that prefix is already a valid block-chain, by induction. Returns whether or not prefix
    + new_char is a valid block-chain.

    We can do this fast, in one iteration over prefix, by keeping track of the smallest character we've
    seen so far, and then for each subsequent character, seeing whether it forms a triple with the new
    character that would cause it to not be a block-chain.
    """

    smallest = None

    for c in prefix:
        if smallest is None or c < smallest:
            smallest = c
        elif smallest < c and c < new_char:
            # invalid block-chain
            return False

    """
    Turns out that we can go one step further than this. Since we know that every other character in
    available has to go after this new_char, we know that for any character in available, the new char
    must be the largest (i.e. nothing can be larger than new_char)
    
    smallest < new_char < character in available

    > We could probably make this faster using a priority queue, but given that my highly optimised
    version in C++ wasn't fast enough, I think I'm missing something more important.
    """

    if smallest < new_char:
        for c in available:
            if new_char < c:
                return False

    return True


def count(prefix, available, target_length) -> int:
    if len(prefix) == target_length:
        # exactly one possible solution
        return 1

    total = 0

    for c in list(available):
        available.remove(c)
        if is_valid_to_add(prefix, c, available):
            prefix.append(c)
            total += count(prefix, available, target_length)
            prefix.pop()
        available.add(c)

    return total


length, prefix = input().split(" ")
length = int(length)

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:length]

available = set(chars) - set(prefix)
prefix = list(prefix)

result = count(prefix, available, length)

print(result)
