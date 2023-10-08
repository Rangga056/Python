# Closure is a function having access to the scope of its parent function
# after the parent function has returned

def parent_fun(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if (coins > 1):
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game


tommy = parent_fun("Tommy", 5)
jenny = parent_fun("Jenny", 1)

tommy()
jenny()
