from functools import reduce
def squared(num): return num * num


print(squared(2))


def addTwo(num): return num + 2
# addTwo = lambda num : num + 2


print(addTwo(3))


def sum_total(a, b): return a + b
# sum = lambda a, b : a + b


print(sum_total(1, 4))

################


def funcBuilder(x):
    return lambda num: num + x


# it will make addTen function with lambda num: num + 10 and accepts num as a params
addTen = funcBuilder(10)
addTwenty = funcBuilder(20)


print(addTen(7))
print(addTwenty(7))

###################

lambda num: num * num

numbers = [3, 12, 22, 4, 65]

squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))

################

# This lambda will return the odd numbers
odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))

##################

nums = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, nums, 10)

print(total)
print(sum(nums, 10))

names = ["rangga", "miftahul", "falah", "yato"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
