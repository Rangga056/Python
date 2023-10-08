name = "rangga"
count = 1
# Global scope variable


def another():
    color = "blue"  # Local scope variable
    # count += 1 #! cant modified the count because its undefined
    global count 
    count += 1 # use global to get the global scope variable and modified it
    print(count) # 2

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)  # This will print the parameter "John"
    greeting("Rangga")


# greeting("John") #* Cant call the function because its in a local scope

another()
