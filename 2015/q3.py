from __future__ import print_function
import math

CHARACTERS = ['A','B','C','D']

try:
    input = raw_input
except:
    pass

a, b, c, d, n = tuple(int(x) for x in input().split())

l = [a, b, c, d]
original_l = [x for x in l]

total = sum(l)

def number_combinations(l, starting_with, n):
    # find the number of combinations starting with the given character
    test_list = [x for x in l]
    test_list[starting_with] -= 1

    if test_list[starting_with] < 0:
        #raise RuntimeError("Unacceptable Start Character")
        return

    a = math.factorial(n - 1)//(math.factorial(test_list[0])*math.factorial(test_list[1])*math.factorial(test_list[2])*math.factorial(test_list[3]))
    return a

# go through recursively

def find_recursively(l, n, nth):
    # go through each of the characters that have an acceptable value
    if n == 1:
        for x in range(len(l)):
            if l[x] != 0:
                print(CHARACTERS[x], end ='')
                return
    
    cumulative_sum = 0
    for x in range(len(l)):
        if l[x] != 0:
            partial_sum = number_combinations(l, x, n)
            cumulative_sum += partial_sum

            if cumulative_sum >= nth:
                new_position = nth - cumulative_sum + partial_sum
                print(CHARACTERS[x], end='')
                # refine the search
                l[x] -= 1
                find_recursively(l, n - 1, nth - cumulative_sum + partial_sum)
                return

find_recursively(l, total, n)
    
def test_q3(n, l):
    print()
    for i in range(1, n + 1):
        y = [x for x in l]
        find_recursively(y, total, i)
        print()

#test_q3(200, original_l)
