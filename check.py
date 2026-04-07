 # List of colors
 Ccolors =["Red", "Blue", "Green", "Yellow", "Orange", "Purple"]

 # Ask the user for sorting preference
 order = input("Enter 'asc' for ascending or 'desc' for descending order: ")

 # Sort the list based on user input
 if order ==("asc".lower()):
  sorted_colors = sorted(Ccolors)
  print("Colors in ascending order:", sorted_colors)
 elif order == ("desc".lower()):
  sorted_colors = sorted(Ccolors, reverse=True)
  print("Colors in descending order:", sorted_colors)
 else:
  print("Invalid input. Please enter 'asc' or 'desc'.")