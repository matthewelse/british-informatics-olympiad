# A solution to the British Informatics Olympiad 2012 Question 1

from time import strftime, gmtime

# number of minutes
a = -1
# number of minutes
b = 0

i = input()

fast = [int(x) for x in i.split()]

actual = 0

while a != b:
    if a == -1:
        a = 0
    a = (a + 60 + fast[0]) % 1440
    b = (b + 60 + fast[1]) % 1440
    actual = (actual + 60) % 1440

print(strftime("%H:%M", gmtime(a*60)))


     
