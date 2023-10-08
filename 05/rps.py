import sys
import random
from enum import Enum # import only 1 from the module 

class RPS(Enum):
  # ALl capitalize for Constant/ const data
  ROCK = 1
  PAPER = 2
  SCISSORS = 3
# RPS(1) will output rock 

print("")
playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("Please must enter the correct number 1, 2, or 3.")

computer_choice = random.choice("123")

computer = int(computer_choice)

print("")
print("You chose " + str(RPS(player)).replace("RPS.", "").title() + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.", "").title() + ".")
print("")

if player == 1 and computer == 3:
  print("You win! 🎉")
elif player == 2 and computer == 1:
  print("You win! 🎉")
elif player == 3 and computer == 2:
  print("You win! 🎉")
elif player == computer:
  print("Tie game! 😲")
else:
  print("Python win! 🐍")