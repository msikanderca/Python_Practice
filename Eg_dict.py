# to add colors to the box:
box = {'color': 'green', 'points': 5}
print(box)
print(type(box))
box["start_position"] = "level"  # to add key-value pair
print(box)
print(box['color'])  # want to know the color of box -- give key and get value
box['color'] = 'red'  # to modify the color from green to red
print(box)
del box['points']  #to delete the key-value pair
print(box)
