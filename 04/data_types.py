import math
# String data type

# literal assigment
first = "Rangga"
last = "Falah"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# # Constructor
# pizza = str("Pepperoni")

# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatination
fullname = first + " " + last
fullname += "!"
print(fullname)

# Number to string
decade = str(2000)
print(decade)

# Multiple Lines
multiline = '''
Hey How are you?

I was just checking in
                            all good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())  # Capitalizing the sentence
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))  # Check the lenght
multiline += "                        "
multiline = "                         " + multiline
print(multiline)

print(len(multiline.strip()))  # removing the whitespace
print(len(multiline.lstrip()))  # left
print(len(multiline.rstrip()))  # right
print("")

# Build
title = "menu".upper()
# centering between 20 character and fill the whitespace with "="
print(title.center(20, "="))
print("Coffe".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$3".rjust(4))
print("Cheesecake".ljust(16, ".") + "$5".rjust(4))
print("")

# String index value
print(first[0])
print(first[-1])  # -1 to get the last index
print(first[0:-1])  # start from the first end before the last
print(first[1:])  # start from the second and to the end

# Methods that returns boolean data
print(first.startswith("R"))
print(first.endswith("a"))
print(first.startswith("r"))

# Boolean Data
myvalue = True  # need to be capital T/F
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric Data Types

# Interger Types
price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price, int))

# Float types
gpa = 3.28
y = float(1.14)
print(type(gpa))

# Complex types
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa))  # absolute value
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))  # rounded to 1 decimal instead of to an interger

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa)) # ceiling value rounded up to the nearest int
print(math.floor(gpa)) # rounded down to the nearest int 

# Casting a string to a number
zipcode = "10011"
zip_value = int(zipcode)


