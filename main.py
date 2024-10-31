
"""
`check_fever` should return `True` if the temperature is `100.4` or higher. For
any lower temperature, it should return `False`.
"""

def check_fever(temperature):
  #YOUR CODE HERE
  if temperature >=100.4:
    return True
  elif temperature < 100.4:
    return False

# Get temperature from user and convert to float
temp = int(input("What's your temperature?"))

if check_fever(temp):
  print(temp)
  print("You have a fever.")
else:
  print(temp)
  print("You don't have a fever.")