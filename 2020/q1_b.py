"""
How many roman numerals from 1 to 3999 inclusive have a look-and-say description
that is also a roman numeral?

List _the descriptions_

To validate the roman numerals, I just calculate a rough guess of what the value
should be for each numeral, and then convert it back to roman numerals. If
they're the same, return true.

Answer is 4:
II, III, IV, IX
"""
import q1

def is_roman(s):
    two_digits = [
        ("CM" , 900),
        ("CD" , 400),
        ("XC" , 90),
        ("XL" , 40),
        ("IX" , 9),
        ("IV" , 4)
    ]

    single_digits = [
        ("M", 1000),
        ("D", 500),
        ("C", 100),
        ("L", 50),
        ("X", 10),
        ("V", 5),
        ("I", 1),
    ]

    value = 0
    
    i = 0
    while i < len(s):
        skip = False

        if len(s) - i >= 2:
            for digits, n in two_digits:
                if s[i:i+2] == digits:
                    i += 2
                    value += n
                    skip = True
                    break

        if skip:
            continue
        
        for digit, n in single_digits:
            if s[i] == digit:
                i += 1
                value += n
                break

    return q1.roman(value) == s

# print("I", is_roman("I"))
# print("IV", is_roman("IV"))
# print("IIII", is_roman("IIII"))

for i in range(3999):
    n = i + 1

    look_and_say = q1.look_and_say(q1.roman(n))

    if is_roman(look_and_say):
        print(look_and_say)
