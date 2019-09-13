def generate_second_dial(n):
    letters = set()
    ring = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result = []
    position = 0

    while len(ring) > 0:
        position += n - 1
        position %= len(ring)

        moved = ring[position]
        ring.remove(moved)
        result.append(moved)

    return result

def encrypt(word, ring):
    result = []
    for c in word:
        char = ord(c) - ord('A')
        encrypted = ring[char]
        result.append(encrypted)
        ring = ring[1:] + ring[:1]
    return ''.join(result)

n, word = input().split(' ')
n = int(n)

dial = generate_second_dial(n)
print(''.join(dial[:6]))
print(encrypt(word, generate_second_dial(n)))