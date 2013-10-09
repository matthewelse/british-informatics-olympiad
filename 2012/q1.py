# A solution to the British Informatics Olympiad 2012 Question 1
# Scores 24/24 Marks

from math import sqrt

n = int(input())
a = int(sqrt(n))
numbers = set(range(2, a))
primes = set()

while numbers:
    curr = min(numbers)
    primes.add(curr)
    numbers.discard(curr)

    for i in range(curr*2, a, curr):
        numbers.discard(i)

factors = 1

for prime in primes:
    if n % prime == 0:
        factors = factors * prime

if factors == 1:
    factors = n

print factors

