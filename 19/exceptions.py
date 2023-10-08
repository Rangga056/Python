class JustNotCoolError(Exception):
  pass

x = 2
# This is similar to try catch in javascript
try:
  raise JustNotCoolError("This is just not cool man!")
  # print(x / 0)
  # if not type(x) is str:
  #   raise TypeError("Only strings are allowed")
except NameError:
  print("NameError means something is probably undefined")
except ZeroDivisionError:
  print("Please do not divide by 0")
except Exception as error:
  print(error)
else:
  print("No Error")
finally:
  # It will reach the finally block even if it raised an error
  print("I'm going to print with or without an error")