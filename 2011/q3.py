# A solution to the British Informatics Olympiad 2011 Question 3
# Scores 24/24
from __future__ import print_function

try:
	input = raw_input
except:
	pass

def number_with_n_digits(n):
	return 9**(n//2)

def nth_with_n_digits(number_of_digits, n):
	if number_of_digits == 0:
		return ""
	if number_of_digits % 2 == 1:
		even = nth_with_n_digits(number_of_digits - 1, n)
		middle = len(even)//2
		return even[:middle] + "5" + even[middle:]
	
	# 9**(n / 2)
	output = ""
	# it needs to start at 0
	n -= 1
	for i in range(number_of_digits // 2):
		n, inner = divmod(n, 9)
		inner += 1
		#n += 1
		output = str(inner) + output + str(10-inner)
	
	return output

nth = int(input())
#nth = 11
sum_so_far = 0
number_of_digits = 0
while sum_so_far < nth:
	number_of_digits += 1
	sum_so_far += number_with_n_digits(number_of_digits)

#print("The number has %i digits!" % number_of_digits)
#print(nth - sum_so_far + number_with_n_digits(number_of_digits))
print(nth_with_n_digits(number_of_digits, nth - sum_so_far + number_with_n_digits(number_of_digits)))


