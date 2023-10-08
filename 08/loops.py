# value = 1
# while value <= 10:
#   print(value)
#   if value == 5:
#     break
#   value += 1

# value = 1
# while value <= 10:
#   value += 1
#   if value == 5: #it will skip 5 or not print and continue the loop
#     continue
#   print(value)
# else:
#   print("value is now equal to " + str(value))


names = ["rangga", "falah", "muhammmad"]
# for x in names:
#   print(x)

# for x in "mississipi":
#   print(x)

# for x in names:
#   if x == "falah":
#     break
# print(x)

# for x in names:
#     if x == "falah":
#         continue
#     print(x)

# for x in range(4):
#   print(x) #it will start from 0

# for x in range(2,4):# starts from 2
#   print(x) #

for x in range(0, 100, 5):  # start from 0 stop before 100 and increment by 5
    print(x)
else:
    print("Glad that\'s over!")

names = ["rangga", "falah", "muhammmad"]
actions = ["code", "eats", "drinks"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
        
