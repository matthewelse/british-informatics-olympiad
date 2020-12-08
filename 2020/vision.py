t, w = input('> ').split()

# Satisfaction for ith telescope
# S = [1, 2, 3, -1, -1, 10]
S = [int(input('> ')) for _ in range(int(t))]
# Path length of jth walker
# U = (23, 24)
U = [int(input('> ')) for _ in range(int(w))]

# Find best pair go back-n-forth
# Pair goodness = sum(pair) * U-index(pair) + sum(0->pair)

# This is optimal because the walker would keep going
# back-n-forth across the pair with highest satisfaction
# as any other path would bring less total satisfaction.
# easy and intuitive to spot if you draw any array.

scores = {u: [] for u in U}
# there is a max telescope that a walker can reach
# which is equal to its u.
for i in range(min(len(S), max(U)) - 1):
    for u in U:
        if i >= u:
            break
        turns = u-i
        # remaining turns would be spent going back-n-forth
        value = ((turns+1)//2)*S[i] + (turns//2)*S[i+1]
        # sum of S to reach best pair
        cost = sum(S[:i])
        scores[u].append(value+cost)

# Since "cost" is added to each score
# The max score is optimal path
# and can be added to total
total = 0
for u in U:
    total += max(scores[u])

print('\n>>>', total)
