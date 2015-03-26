from __future__ import print_function

try:
    input = raw_input
except:
    pass

word = input()

def chunk(word, first=False):
    if len(word) == 1:
        return [[word]]
    else:
        chunks = []
        if not first:
            chunks.append([word])
        for i in range(1,len(word)):
            for c in chunk(word[i:]):
                chunks.append([word[:i]] + c)
        return chunks

possible_chunks = [tuple(x) for x in chunk(word, True)]
good_chunks = [x for x in possible_chunks if tuple(reversed(x)) == x]
print(len(good_chunks))


def part_b():
    print(good_chunks)

#part_b()
