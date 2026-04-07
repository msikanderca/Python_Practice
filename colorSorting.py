# List of colors
colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple"]

# Ask the user for sorting preference
order = input("Enter 'asc' for ascending or 'desc' for descending order: ").strip().lower()

# Sort the list based on user input
if order == "asc":
    sorted_colors = sorted(colors)
    print("Colors in ascending order:", sorted_colors)
elif order == "desc":
    sorted_colors = sorted(colors, reverse=True)
    print("Colors in descending order:", sorted_colors)
else:
    print("Invalid input. Please enter 'asc' or 'desc'.")







