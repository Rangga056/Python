# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocal="plants", guitar="page")

print(band)
print(band2)
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all value
print(band.values())

# List of key/value pairs as tuples
print(band.items())

# verify if key exist
print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Remove  items
print(band.pop("bass"))

band["drums"] = "RRRRR"
print(band.popitem())  # remove the last key value pair as tuple
print(band)

# Delete and clear
band["drums"] = "RRRRR"
del band["drums"]

band2.clear()
print(band2)

del band2

# Copy dictionaries
# band2 = band # Create a reference
# print("bad copy")

band2 = band.copy()
band2["drums"] = "falah"
print(band2)

# or use the dict constructor
band3 = dict(band)
print(band3)

# Nested dictionaries
member1 = {
    "name": "Ranffa",
    "Instrument": "Vocals"
}
member2 = {
    "name": "ffffa",
    "Instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
print("")
print(band["member1"]["name"])

# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))  # using the constructor

print(nums)
print(type(nums))
print(len(nums2))

# No duplicates allowed and it will be in order
nums = {1, 2, 2, 3}
print(nums)

# True is a duplicate of 1, false is a dupe for 0
nums = {1, True, 2, False, 0}
print(nums)  # it will print the first one of the dupe

# Check if a value is in a set
print(2 in nums)

# * You cannot refer to an element in the set with an index or a key

# Add a new element to a set
nums.add(8)
print(nums)

# You can add element from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# You can use update with lists, tuples, and dictionaries, too.

# Merge 2 sets to create a new set
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates from the different sets
one = {1, 2, 3, 9}
two = {4, 2, 1}

one.intersection_update(two)
print(one)  # Output {1,2}

# Keep everything except the duplicates from the different sets
one = {1, 2, 3, 9}
two = {4, 2, 1}

one.symmetric_difference_update(two)
print(one)  # output {3,4,9}
