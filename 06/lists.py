users = ["Rangga", "Falah", "Rizz"]
data = ["ra", 23, False]
empylist = []

print("Rangga" in users)

print(users[0])
print(users[-1])

print(users.index("Rangga"))

print(users[0:1])
print(users[1:])
print(len(users))

# users.append("Eclipse")

# users += ["Jason", "sarah"]
# print(users)

# users.extend(["Roger", "Bravo"])
# print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")  # insert Bob in the first position in the list

# insert after the second position without replacing any data
users[2:2] = ["eddie", "alex"]
print(users)

users.remove("Bob")

print(users.pop())

del users[0]  # delete the first value in the list

# del data to delete the list
data.clear()  # to empty the list
print(data)

users[1:2] = ["rangga"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 36]
nums.reverse()
print(nums)

# nums.sort(reverse=True) # Sort descending
# print(nums)

# Sorting without modifying the original list
print(sorted(nums, reverse=True))
print(nums)

# copy the nums list
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)

print(type(nums))

mylist = list([1, "Ran", False])
print(mylist)

# ! Tuples
mytuple = tuple(("Rangga", 22, True))
anothertuple = (1, 2, 2, 4)

print(mytuple)
print(type(mytuple))

newlist = list(mytuple)
newlist.append("neil")
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hei) = anothertuple
print(one)
print(two)
print(hei)

print(anothertuple.count(2))  # counting how many 2 inside the tuple 
