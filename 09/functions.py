def hello_world(word):
    print(word)


hello_world("hello world")


def sum(num1=0, num2=0):  
    # set the num2 default value to 3 when theres no 2nd parameter in when the func is called
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2


total = sum(10, 10)
print(total)


def multiple_items(*args): # use * when u dont know how many parameters goin to be 
    print(args)
    print(type(args)) # tuples


multiple_items("rangga", "falah")


def multi_named_items(**kwargs): # Keywrod Arguments
    print(kwargs)
    print(type(kwargs)) # dictionaries

multi_named_items(first = "Rangga", last = "Falah")
