import os
# r = read
# a = append
# w = write
# x = create

# Read - err if it doesn't exist

f = open("names.txt")  # the default is "r" read
# print(f.read(4)) #read the first 4 characters
# print(f.read())

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("ttxct.txt")
    print(f.read())
except:
    print("The file you want to doesn't exist")
finally:
    f.close()

# Append creates the file if it doesn't exist

f = open("names.txt", "a")
f.write("Neil")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (Overwrite)
f = open("context.txt", "w")
f.write("I deleted all of context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Open a file for writing, creates the file if it doesn't exist
f = open("name_list.txt", "w")
f.close()

# Creates the specified file but returns an error if the file already exists
if not os.path.exists("rangga.txt"):
    f = open("rangga.txt", "x")
    f.close()

# Delete a file

# Avoid an error if it doesn't exists
if os.path.exists("names_list"):
    os.remove("names_list.txt")
else:
    print("The file you wish to delete doesn't exists")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
