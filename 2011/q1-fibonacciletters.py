# A solution to the British Informatics Olympiad 2011 Question 1
# Scores 24/24

def fib(a, b):
	a = ord(a) - 65
	b = ord(b) - 65

	return chr(((a + b) % 26) + 66)

_input = 'B I 987654'.split()

a = _input[0]
b = _input[1]
n = int(_input[2])

if n == 1:
	print a
elif n == 2:
	print b
else:
	for i in range(n - 2):
		new = fib(a, b)
		a = b
		b = new
	
	print new
