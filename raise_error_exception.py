#Raise Exceptions

try:
  x = int(input("Enter a number: "))
  if x < 0:
    raise ValueError("Number must be non-negative")
  print("You entered:", x)
except ValueError as e:
  print("Error:", e)
